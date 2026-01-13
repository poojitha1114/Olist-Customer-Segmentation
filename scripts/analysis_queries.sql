-- Query 1: Top 5 Customers
SELECT customer_id, monetary, segment 
FROM rfm_table 
ORDER BY monetary DESC 
LIMIT 5;

-- Query 2: Segment Summary
SELECT 
    segment, 
    COUNT(customer_id) AS total_customers, 
    SUM(monetary) AS total_revenue
FROM rfm_table 
GROUP BY segment;