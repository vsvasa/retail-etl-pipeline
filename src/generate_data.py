import pandas as pd
import numpy as np
import random
import os
from faker import Faker
from datetime import datetime, timedelta
from utils import setup_logger

logger = setup_logger()

fake = Faker() # initializes faker instance
random.seed(42) # sets seed for random module
np.random.seed(42) # sets seed for numpy module

def get_next_id(filepath,id_column):
    if os.path.exists(filepath):
        df = pd.read_csv(filepath)
        if len(df)>0:
            df[id_column] = pd.to_numeric(df[id_column], errors='coerce')
            return int(df[id_column].max()) + 1
    return 1
       
def append_csv(df,filepath):
    file_exists = os.path.exists(filepath)
    df.to_csv(filepath, mode='a' if file_exists else 'w', header=not file_exists, index=False)
        

def generate_customers(num_customers=10000):
    """Generates a DataFrame of customer data."""
    customers = []
    start_id = get_next_id("data/raw/customers.csv", "customer_id")
    for customer_id in range(start_id, start_id + num_customers):   
        customers.append({
            "customer_id":customer_id,
            "first_name":fake.first_name(),
            "last_name":fake.last_name(),
            "email":fake.unique.email(),
            "city":fake.city(),
            "state":fake.state(),
            "country":fake.country(),
            "added_date":fake.date_between(start_date='-2y', end_date='today'),
            "added_by":"ADMIN",
            "is_active":np.random.randint(0,2)
        })
    
    return pd.DataFrame(customers)
    
def generate_products(num_products = 1000):
    products = []
    categories = ['Electronics','Clothing','Home & Kitchen','Beauty','Books','Sports','Toys']
    start_id = get_next_id("data/raw/products.csv", "product_id")
    for product_id in range(start_id, start_id + num_products):
        products.append({
            "product_id":product_id,
            "product_name":fake.word().capitalize(),
            "category":random.choice(categories),
            "price":round(random.uniform(0,1000),2),
            "added_date":fake.date_between(start_date='-2y', end_date='today'),
            "added_by":"ADMIN",
        })
    return pd.DataFrame(products)
    
def generate_orders(num_orders=100000,num_customers=10000):
    orders = []
    start_id = get_next_id("data/raw/orders.csv", "order_id")
    for order_id in range(start_id, start_id + num_orders):
        orders.append({
        "order_id":order_id,
        "customer_id":np.random.randint(1,num_customers),
        "order_date":fake.date_between(start_date='-2y',end_date='today'),
        "amount":round(random.uniform(0, 50000),2),
        "added_date":fake.date_between(start_date='-2y', end_date='today'),
        "added_by":"ADMIN"
    })
    return pd.DataFrame(orders)

def generate_sales(orders_df, num_sales=500000, num_products=1000):

    sales = []

    # Convert order_ids once
    order_ids = orders_df["order_id"].tolist()
    start_id = get_next_id("data/raw/sales.csv", "sale_id")
    for sale_id in range(start_id, start_id + num_sales):

        sales.append({
            "sale_id": sale_id,
            "order_id": random.choice(order_ids),
            "product_id": np.random.randint(1, num_products + 1),
            "quantity": np.random.randint(1, 10),
            "sale_amount": round(random.uniform(0, 2000), 2),
            "added_date": datetime.now(),
            "added_by":"ADMIN"
        })

    return pd.DataFrame(sales)

if __name__ == "__main__":
    print("Generating Customers...")
    customers_df = generate_customers()
    logger.info(f"Total no of customeres : {len(customers_df)} ")
    print("Generating Products...")
    products_df = generate_products()
    logger.info(f"Total no of products : {len(products_df)} ")
    print("Generating Orders...")
    orders_df = generate_orders()
    logger.info(f"Total no of orders : {len(orders_df)} ")

    print("Generating Sales...")
    sales_df = generate_sales(orders_df)
    logger.info(f"Total no of sales : {len(sales_df)} ")
    print("Data Generation Completed.")
    

    print("exporting data to CSV files...")
    append_csv(customers_df,"data/raw/customers.csv")
    append_csv(products_df,"data/raw/products.csv")
    append_csv(orders_df,"data/raw/orders.csv")
    append_csv(sales_df,"data/raw/sales.csv")       

    print("Data Exported Successfully.")
    
        

        