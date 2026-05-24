CREATE TABLE IF NOT EXISTS customers (
    customer_id INT(11) PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100),
    email VARCHAR(50) UNIQUE,
    city VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(100),
    added_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    added_by VARCHAR(100) NOT NULL DEFAULT 'ADMIN',
    is_active TINYINT(1) NOT NULL DEFAULT 1
);
CREATE TABLE IF NOT EXISTS products (
    product_id INT(11) PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(50) NOT NULL,
    category VARCHAR(25),
    price INT(10) NOT NULL,
    added_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    added_by VARCHAR(100) NOT NULL DEFAULT 'ADMIN'
);
CREATE TABLE IF NOT EXISTS orders (
    order_id INT(11) PRIMARY KEY AUTO_INCREMENT,
    customer_id INT(11),
    order_date DATE NOT NULL,
    amount FLOAT(10) NOT NULL,
    added_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    added_by VARCHAR(100) NOT NULL DEFAULT 'ADMIN'
);
CREATE TABLE IF NOT EXISTS sales (
    sale_id INT(11) PRIMARY KEY AUTO_INCREMENT,
    order_id INT(11) NOT NULL,
    product_id INT(11) NOT NULL,
    quantity INT(11) NOT NULL,
    sale_amount FLOAT(10) NOT NULL,
    high_value_sale FLOAT(10) NOT NULL,
    added_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    added_by VARCHAR(100) NOT NULL DEFAULT 'ADMIN'
);
CREATE TABLE IF NOT EXISTS etl_metadata (
    table_name VARCHAR(100) PRIMARY KEY,
    last_loaded_timestamp DATETIME
);