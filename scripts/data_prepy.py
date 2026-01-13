import pandas as pd
import sqlite3
import datetime as dt
import os

# Create folders if they don't exist
os.makedirs('data', exist_ok=True)
os.makedirs('output', exist_ok=True)

# --- STEP 1: LOAD DATA ---
try:
    # Loading the three essential files for your specific workflow
    orders = pd.read_csv('data/olist_orders_dataset.csv')
    payments = pd.read_csv('data/olist_order_payments_dataset.csv')
    customers = pd.read_csv('data/olist_customers_dataset.csv')
    print("Files loaded successfully.")
except FileNotFoundError as e:
    print(f"Error: {e}. Ensure CSVs are in the 'data/' folder.")
    exit()

# --- STEP 2: CLEAN & MERGE ---
orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])

# A. Link Orders and Payments using 'order_id'
# This gives us the date and the money together
order_payments = pd.merge(orders, payments, on='order_id')

# B. Link the result with Customers using 'customer_id'
# This connects the order to the actual unique person
df = pd.merge(order_payments, customers, on='customer_id')

# Filter for delivered orders to ensure we only count successful revenue
df = df[df['order_status'] == 'delivered']

# --- STEP 3: CALCULATE RFM METRICS ---
latest_date = df['order_purchase_timestamp'].max() + dt.timedelta(days=1)

# IMPORTANT: Grouping by 'customer_unique_id' ensures we track the PERSON, not the order.
rfm = df.groupby('customer_unique_id').agg({
    'order_purchase_timestamp': lambda x: (latest_date - x.max()).days, # Recency
    'order_id': 'nunique',                                             # Frequency
    'payment_value': 'sum'                                             # Monetary
})

rfm.columns = ['Recency', 'Frequency', 'Monetary']

# --- STEP 4: QUINTILE SCORING (1-5) ---
rfm['R'] = pd.qcut(rfm['Recency'], 5, labels=[5, 4, 3, 2, 1]) 
rfm['F'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1, 2, 3, 4, 5])
rfm['M'] = pd.qcut(rfm['Monetary'], 5, labels=[1, 2, 3, 4, 5])

# --- STEP 5: PROFESSIONAL SEGMENT MAPPING ---
rfm['RF_Score'] = rfm['R'].astype(str) + rfm['F'].astype(str)

segs = {
    r'[4-5][4-5]': 'Champions',
    r'[2-5][3-5]': 'Loyal Customers',
    r'[3-5][1-2]': 'Potential Loyalists',
    r'2[1-2]': 'At Risk / Need Attention',
    r'1[1-5]': 'Lost / Hibernating'
}

rfm['Segment'] = rfm['RF_Score'].replace(segs, regex=True)

# --- STEP 6: EXPORT ---
rfm.to_csv('output/rfm_output.csv')

conn = sqlite3.connect('olist_data.db')
rfm.to_sql('rfm_table', conn, if_exists='replace')

total_revenue = rfm['Monetary'].sum()
print(f"\n--- SUCCESS: PYTHON PHASE COMPLETE ---")
print(f"Total Revenue Verified: ${total_revenue:,.2f}")
print("\nSegment Distribution (%):")
print(rfm['Segment'].value_counts(normalize=True) * 100)

conn.close()
