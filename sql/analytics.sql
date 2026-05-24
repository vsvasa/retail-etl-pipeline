-- =========================================
-- Retail ETL Pipeline KPI Queries
-- =========================================
-- 1. Total Revenue
SELECT ROUND(SUM(sale_amount), 2) AS total_revenue
FROM sales;
-- =========================================
-- 2. Total Orders
SELECT COUNT(*) AS total_orders
FROM orders;
-- =========================================
-- 3. Total Customers
SELECT COUNT(*) AS total_customers
FROM customers;
-- =========================================
-- 4. Average Order Value
SELECT ROUND(AVG(amount), 2) AS avg_order_value
FROM orders;
-- =========================================
-- 5. Monthly Revenue Trend
SELECT YEAR(o.order_date) AS order_year,
    MONTH(o.order_date) AS order_month,
    ROUND(SUM(s.sale_amount), 2) AS revenue
FROM sales s
    JOIN orders o ON s.order_id = o.order_id
GROUP BY 1,
    2
ORDER BY 1,
    2;
-- =========================================
-- 6. Top 10 Customers
SELECT c.customer_id,
    CONCAT(
        c.first_name,
        ' ',
        c.last_name
    ) AS customer_name,
    ROUND(SUM(o.amount), 2) AS total_spent
FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
GROUP BY 1,
    2
ORDER BY total_spent DESC
LIMIT 10;
-- =========================================
-- 7. Top Selling Products
SELECT p.product_name,
    SUM(s.quantity) AS total_quantity
FROM sales s
    JOIN products p ON s.product_id = p.product_id
GROUP BY 1
ORDER BY total_quantity DESC
LIMIT 10;
-- =========================================
-- 8. High Value Sales %
SELECT ROUND(
        SUM(high_value_sale) / COUNT(*) * 100,
        2
    ) AS high_value_sale_percentage
FROM sales;
-- =========================================
-- 9. Customer Order Ranking
SELECT customer_id,
    COUNT(order_id) AS total_orders,
    RANK() OVER(
        ORDER BY COUNT(order_id) DESC
    ) AS customer_rank
FROM orders
GROUP BY customer_id;