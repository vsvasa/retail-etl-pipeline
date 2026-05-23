import pandas as pd


def transform_customers_data(df):

    # Remove duplicates
    df = df.drop_duplicates()
    
    #Handle null emails
    df = df.dropna(subset=['email'])

    # Standardize names

    df['first_name'] = df['first_name'].str.title()
    df['last_name'] = df['last_name'].str.title()
    df['email'] = df['email'].str.lower()

    #convert datetime

    df['created_date'] = pd.to_datetime(df['created_date'])
    df['updated_date'] = pd.to_datetime(df['updated_date'])

    return df


def transform_products_data(df):
    # Remove duplicates
    df = df.drop_duplicates()

    # Remove invalid prices

    df = df[df['price'] > 0]

    # Standerdize category names
    df['category'] = df['category'].str.title()

    return df


def transform_orders_data(df):
    # Remove duplicates
    df = df.drop_duplicates()
    
    # convert order_date
    df['order_date'] = pd.to_datetime(df['order_date'])
    
    # remove invalid amounts
    df = df[df['amount'] > 0]

    # Add orders month
    df['order_month'] = df['order_date'].dt.month

    # Add order Year
    df['order_year'] = df['order_date'].dt.year
    
    # Select final columns
    df = df[
        [
            "order_id",
            "customer_id",
            "order_date",
            "amount"
        ]
    ]
    return df


def transform_sales_data(df):
    # remove duplicates
    df = df.drop_duplicates()
    
    #remove invalid values
    df = df[(df['quantity'] > 0) & (df['sale_amount'] > 0)]

    # Convert datetime
    df['last_updated'] = pd.to_datetime(df['last_updated'])

    # Add High sales flag

    df['high_value_sale'] = df['sale_amount'] > 1000
    
    return df