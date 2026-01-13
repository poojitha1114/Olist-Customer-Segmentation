-- 1. Total Revenue Check
SELECT printf('$%,.2f', SUM(Monetary)) AS Grand_Total FROM rfm_table;

-- 2. Segment Analysis
SELECT 
    Segment, 
    COUNT(*) as Customer_Count, 
    printf('$%,.2f', SUM(Monetary)) as Total_Revenue
FROM rfm_table
GROUP BY Segment
ORDER BY SUM(Monetary) DESC;

-- 3. High-Value Action List (Champions)
-- We use customer_unique_id because that is the primary key of our RFM table
SELECT 
    customer_unique_id, 
    Recency, 
    Frequency, 
    printf('$%,.2f', Monetary) as Lifetime_Value
FROM rfm_table 
WHERE Segment = 'Champions' 
ORDER BY Monetary DESC 
LIMIT 10;
