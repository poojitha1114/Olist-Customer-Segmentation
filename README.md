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

### 1. Metrics Calculation
* **Recency (R):** Days since the customer's last purchase ($Date_{max} - Date_{last\_order}$).
* **Frequency (F):** Count of unique `order_id`s per customer.
* **Monetary (M):** Total `payment_value` summed for each unique customer.

### 2. Statistical Scoring (Quintiles)
I used `pd.qcut` to rank customers into 5 equal groups. A score of **5** represents the top 20% of the database for that metric (e.g., the most recent or highest spending customers).

### 3. Segment Mapping (Regex)
Using **Regular Expressions**, I combined **R** and **F** scores into business personas:

| Segment | RF Score Range | Strategy |
| :--- | :--- | :--- |
| **Champions** | `[4-5][4-5]` | Reward them. They can be early adopters for new products. |
| **Loyal Customers** | `[2-5][3-5]` | Up-sell higher value products. |
| **Potential Loyalists**| `[3-5][1-2]` | Offer loyalty programs or "second purchase" discounts. |
| **At Risk** | `2[1-2]` | Send personalized "We Miss You" emails before they churn. |
| **Lost / Hibernating**| `1[1-5]` | Don't overspend on re-acquisition; focus on low-cost reach. |

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
