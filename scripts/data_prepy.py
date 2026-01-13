import pandas as pd
import sqlite3
import os

# Create folders
os.makedirs('data', exist_ok=True)
os.makedirs('outputs', exist_ok=True)

def run_pipeline():
    # Load
    orders = pd.read_csv('data/olist_orders_dataset.csv')
    payments = pd.read_csv('data/olist_order_payments_dataset.csv')
    customers = pd.read_csv('data/olist_customers_dataset.csv')

    # Merge
    df = orders.merge(payments, on='order_id').merge(customers, on='customer_id')
    df = df[df['order_status'] == 'delivered']
    df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

    # RFM Logic
    snapshot = df['order_purchase_timestamp'].max() + pd.Timedelta(days=1)
    rfm = df.groupby('customer_unique_id').agg({
        'order_purchase_timestamp': lambda x: (snapshot - x.max()).days,
        'order_id': 'nunique',
        'payment_value': 'sum'
    }).reset_index() # Important: This makes customer_unique_id a real column

    rfm.columns = ['customer_id', 'recency', 'frequency', 'monetary']

    # Scoring
    rfm['r'] = pd.qcut(rfm['recency'], 5, labels=[5, 4, 3, 2, 1])
    rfm['f'] = pd.qcut(rfm['frequency'].rank(method="first"), 5, labels=[1, 2, 3, 4, 5])
    rfm['m'] = pd.qcut(rfm['monetary'], 5, labels=[1, 2, 3, 4, 5])

    # Segmenting
    rfm['segment'] = (rfm['r'].astype(str) + rfm['f'].astype(str)).replace({
        r'[4-5][4-5]': 'Champions',
        r'[2-5][3-5]': 'Loyal',
        r'[3-5][1-2]': 'Potential',
        r'2[1-2]': 'At Risk',
        r'1[1-5]': 'Lost'
    }, regex=True)

    # EXPORT
    rfm.to_csv('outputs/rfm_output.csv', index=False)
    
    conn = sqlite3.connect('olist_data.db')
    rfm.to_sql('rfm_table', conn, if_exists='replace', index=False)
    conn.close()
    print("DONE: Database created with columns: customer_id, recency, frequency, monetary, segment")

run_pipeline()