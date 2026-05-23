# Data Engineering Concepts Implemented

## Referential Integrity
Implemented referential integrity by ensuring all foreign key references point to valid parent records.  
For example:
- `orders.customer_id` references valid `customers.customer_id`
- `sales.order_id` references valid `orders.order_id`
- `sales.product_id` references valid `products.product_id`

This was achieved using controlled random ID generation and parent key lookups during synthetic data generation.

---

## Synthetic Data Engineering
Built a realistic synthetic retail dataset generation framework using the Faker library and randomized transaction simulation techniques.

Generated:
- Customer profiles
- Product catalogs
- Retail orders
- Sales transactions
- Geographic data
- Timestamped events

This simulated production-style raw ingestion datasets for ETL processing.

---

## Scalable Dataset Design
Designed parameterized data generation functions capable of producing scalable datasets ranging from thousands to millions of records.

Examples:
- 10K customers
- 100K orders
- 500K+ sales transactions

The framework supports easy scalability without modifying business logic.

---

## Data Generation Optimization
Optimized transaction generation performance by replacing repeated DataFrame sampling operations with in-memory list-based lookups.

### Before Optimization
Used:
```python
orders_df.sample(1).iloc[0]