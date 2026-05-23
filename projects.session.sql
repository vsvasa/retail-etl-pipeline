CREATE TABLE IF NOT EXISTS customers (
    customer_id INT(11) PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100),
    email VARCHAR(50) UNIQUE,
    city VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(50),
    created_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    created_by VARCHAR(100) NOT NULL DEFAULT 'ADMIN',
    updated_date DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    updated_by VARCHAR(100) NOT NULL DEFAULT 'ADMIN',
    active_status TINYINT(1) NOT NULL DEFAULT 1
);
CREATE TABLE IF NOT EXISTS products (
    product_id INT(11) PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(50) NOT NULL,
    category VARCHAR(25),
    price INT(10) NOT NULL
);
CREATE TABLE IF NOT EXISTS orders (
    order_id INT(11) PRIMARY KEY AUTO_INCREMENT,
    customer_id INT(11),
    order_date DATE NOT NULL,
    amount FLOAT(10) NOT NULL
);
CREATE TABLE IF NOT EXISTS sales (
    sale_id INT(11) PRIMARY KEY AUTO_INCREMENT,
    order_id INT(11) NOT NULL,
    product_id INT(11) NOT NULL,
    quantity INT(11) NOT NULL,
    sale_amount FLOAT(10) NOT NULL,
    last_updated DATETIME DEFAULT CURRENT_TIMESTAMP -- ✅ removed duplicate 'timestamp'
);