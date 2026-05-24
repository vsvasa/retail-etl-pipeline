-- =========================================
-- Retail ETL Validation Queries
-- =========================================
-- 1. Duplicate Customer Emails
SELECT email,
    COUNT(*) AS duplicate_count
FROM customers
GROUP BY email
HAVING COUNT(*) > 1;
-- =========================================
-- 2. Null Customer Emails
SELECT COUNT(*) AS null_emails
FROM customers
WHERE email IS NULL;
-- =========================================
-- 3. Negative Product Prices
SELECT *
FROM products
WHERE price <= 0;
-- =========================================
-- 4. Invalid Order Amounts
SELECT *
FROM orders
WHERE amount <= 0;
-- =========================================
-- 5. Invalid Sales Quantities
SELECT *
FROM sales
WHERE quantity <= 0;
-- =========================================
-- 6. Orphan Orders
-- Orders without customers
SELECT o.*
FROM orders o
    LEFT JOIN customers c ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;
-- =========================================
-- 7. Orphan Sales
-- Sales without orders
SELECT s.*
FROM sales s
    LEFT JOIN orders o ON s.order_id = o.order_id
WHERE o.order_id IS NULL;
-- =========================================
-- 8. Orphan Product References
SELECT s.*
FROM sales s
    LEFT JOIN products p ON s.product_id = p.product_id
WHERE p.product_id IS NULL;
-- =========================================
-- 9. Future Order Dates
SELECT *
FROM orders
WHERE order_date > CURDATE();