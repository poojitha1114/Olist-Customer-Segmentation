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

## 📈 Key Insights
* **Total Revenue:** $15.42M.
* **Actionable Segments:** Identified 'At Risk' and 'Lost' customers to help the marketing team focus on retention strategies
* **Top Customers:** Successfully isolated 'Champions'—our most valuable customer group

## 🛠️ Tools Used
* **Python:** Pandas, NumPy
* **SQL:** SQLite
* **BI:** Power BI Desktop
