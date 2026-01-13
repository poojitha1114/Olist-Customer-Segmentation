# E-Commerce Customer Segmentation (RFM Analysis)

## 📊 Project Overview
This project provides an end-to-end data analytics solution for the Olist E-commerce dataset. It automates the process of cleaning raw transaction data, performing RFM (Recency, Frequency, Monetary) scoring, and visualizing customer health through an interactive Power BI dashboard.

## 🚀 The Pipeline
1.  **Extract & Transform (Python):** Cleaned 100k+ rows of order data. Calculated Recency, Frequency, and Monetary values to assign segments.
2.  **Load (SQL/SQLite):** Stored the processed data into a local SQLite database for structured querying and validation.
3.  **Visualize (Power BI):** Designed a dashboard to track **$15.42M in total revenue** and identify high-risk customer segments.

## 📂 Folder Structure
* `data/`: Raw CSV files from Olist.
* `scripts/`: 
    * `data_prep.py`: Python ETL script.
    * `analysis_queries.sql`: SQL validation queries.
* `output/`: Processed RFM CSV file.
* `olist_data.db`: The generated SQLite database.
* `power_BI.pdf`: A static snapshot of the final dashboard.

## 🧮 RFM Segmentation Logic

### 1. Metrics Calculation
* **Recency (R):** Days since the customer's last purchase ($Date_{max} - Date_{last\_order}$).
* **Frequency (F):** Count of unique `order_id`s per customer.
* **Monetary (M):** Total `payment_value` summed for each unique customer.

### 2. Statistical Scoring (Quintiles)
I used `pd.qcut` to rank customers into 5 equal groups. A score of **5** represents the top 20% of the database for that metric (e.g., the most recent or highest spending customers).

### 3. Segment Mapping (Regex)
Each customer is assigned a score from **1 (Lowest)** to **5 (Highest)** for Recency (R) and Frequency (F). We use these scores to define the following business segments:

| Segment | Recency Score | Frequency Score | Business Strategy |
| :--- | :--- | :--- | :--- |
| **Champions** | 4, 5 | 4, 5 | Reward them. They are your brand ambassadors. |
| **Loyal Customers** | 3, 4, 5 | 3, 4, 5 | High value. Focus on up-selling and cross-selling. |
| **Potential Loyalists**| 4, 5 | 1, 2 | New customers. Offer a second-purchase discount. |
| **At Risk** | 1, 2 | 3, 4, 5 | Previously loyal. Send a "We Miss You" coupon. |
| **Lost / Hibernating**| 1, 2 | 1, 2 | Lowest value. Focus on low-cost reactivation. |

## 📈 Key Insights
* **Total Revenue:** $15.42M.
* **Actionable Segments:** Identified 'At Risk' and 'Lost' customers to help the marketing team focus on retention strategies
* **Top Customers:** Successfully isolated 'Champions'—our most valuable customer group

## 🧠 Technical Skills Demonstrated
1. **Python**: Data grouping, datetime math, and statistical quintile scoring.
2. **SQL**: CTEs for data validation and segment verification.
3. **Power BI**: Interactive dashboard design with DAX measures and context-sensitive filtering .

## 🛠️ How to Run Locally
1. **Prerequisites**

* Install Python and Pandas: pip install pandas.
* Power BI Desktop (to view the .pbix file).

2. **Execution Steps**
* Clone this repository to your local machine.
* Place the Olist CSV files in the `data/` folder.
* Run the Python script:
   ```bash
   python scripts/data_prep.py
   ```
* Open olist_data.db in any SQL editor to verify the $15.42M total using analysis_queries.sql.
* Open the .pbix file in Power BI Desktop to interact with the segments.
