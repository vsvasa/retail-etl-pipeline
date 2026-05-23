import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker() # initializes faker instance
random.seed(42) # sets seed for random module
np.random.seed(42) # sets seed for numpy module


def generate_customers(num_customers=10000):
    """Generates a DataFrame of customer data."""
    customers = []

    for customer_id in range(1, num_customers + 1):
        customers.append({
            "customer_id":customer_id,
            "first_name":fake.first_name(),
            "last_name":fake.last_name(),
            "email":fake.unique.email(),
            "city":fake.city(),
            "state":fake.state(),
            "country":fake.country(),
            "created_date":fake.date_between(start_date='-2y', end_date='today'),
            "created_by":"ADMIN",
            "updated_date":datetime.now(),
            "updated_by":"ADMIN",
            "active_status":np.random.randint(0,2)
        })
    
    return pd.DataFrame(customers)
    
def generate_products(num_products = 1000):
    products = []
    categories = ['Electronics','Clothing','Home & Kitchen','Beauty','Books','Sports','Toys']

    for product_id in range(1,num_products + 1):
        products.append({
            "product_id":product_id,
            "product_name":fake.word().capitalize(),
            "category":random.choice(categories),
            "price":round(random.uniform(10,1000),2)
        })
    return pd.DataFrame(products)
    
def generate_orders(num_orders=100000,num_customers=10000):
    orders = []

    for order_id in range(1,num_orders + 1):
        orders.append({
        "order_id":order_id,
        "customer_id":np.random.randint(1,num_customers),
        "order_date":fake.date_between(start_date='-2y',end_date='today'),
        "amount":round(random.uniform(100, 50000),2)
    })
    return pd.DataFrame(orders)

def generate_sales(orders_df, num_sales=500000, num_products=1000):

    sales = []

    # Convert order_ids once
    order_ids = orders_df["order_id"].tolist()

    for sale_id in range(1, num_sales + 1):

        sales.append({
            "sale_id": sale_id,
            "order_id": random.choice(order_ids),
            "product_id": np.random.randint(1, num_products + 1),
            "quantity": np.random.randint(1, 10),
            "sale_amount": round(random.uniform(20, 2000), 2),
            "last_updated": datetime.now()
        })

    return pd.DataFrame(sales)

if __name__ == "__main__":
    print("Generating Customers...")
    customers_df = generate_customers()

    print("Generating Products...")
    products_df = generate_products()

    print("Generating Orders...")
    orders_df = generate_orders()

    print("Generating Sales...")
    sales_df = generate_sales(orders_df)

    print("Data Generation Completed.")
    

    print("exporting data to CSV files...")
    customers_df.to_csv("data/raw/customers.csv",index=False)
    products_df.to_csv("data/raw/products.csv",index=False)
    orders_df.to_csv("data/raw/orders.csv",index=False)
    sales_df.to_csv("data/raw/sales.csv",index=False)       

    print("Data Exported Successfully.")
    
        

        