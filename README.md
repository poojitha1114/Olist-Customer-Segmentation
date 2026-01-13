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

## 🛠️ How to Run Locally
1. **Prerequisites**

* Install Python and Pandas: pip install pandas.
* Power BI Desktop (to view the .pbix file).

2. **Execution Steps**
* Clone the Repo: git clone https://github.com/YOUR_USERNAME/your-repo-name.git.
* Process Data: Run python scripts/data_prep.py. This cleans the 100k rows and calculates Recency, Frequency, and Monetary scores.
* Database Check: Open olist_data.db to verify the $15.42M revenue total via SQL.
* View Dashboard: Open data_analyst.pbix. Use the Slicer buttons (At Risk, Champions, etc.) to filter the customer table .

## 🧠 Technical Skills Demonstrated
1. **Python**: Data grouping, datetime math, and statistical quintile scoring.
2. **SQL**: CTEs for data validation and segment verification.
3. **Power BI**: Interactive dashboard design with DAX measures and context-sensitive filtering .
