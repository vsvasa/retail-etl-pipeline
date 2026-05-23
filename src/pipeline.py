from extract import extract_csv
from transform import transform_customers_data,transform_products_data,transform_orders_data,transform_sales_data
from load import load_data,create_conn
from utils import setup_logger

logger = setup_logger()

def main():
    try:
        print("Starting the ETL pipeline")
        logger.info("ETL pipeline started ")
        #------------- Extract Layer Engineering -------------------
        logger.info("Extract layer Engineering started")
        logger.info("Extracting Customers data")
        customer_df = extract_csv("data/raw/customers.csv",["customer_id","first_name","last_name","email"])
        logger.info(f"Customers data loaded successfully: {len(customer_df)} rows")
        
        logger.info("Extracting Products Data")
        products_df = extract_csv("data/raw/products.csv",["product_id","product_name","category","price"])
        logger.info(f"Products data loaded successfully: {len(products_df)} rows")

        logger.info("Extracting Orders Data")
        orders_df = extract_csv("data/raw/orders.csv",["order_id","customer_id","order_date","amount"]) 
        logger.info(f"Orders data loaded successfully: {len(orders_df)} rows")

        logger.info("Extracting Sales Data")
        sales_df = extract_csv("data/raw/sales.csv",["sale_id","order_id","product_id","quantity","sale_amount"])
        logger.info(f"Sales data loaded successfully: {len(sales_df)} rows")
        logger.info("Extract layer Engineering ended")

        # ----------- Transform Layer Engineering
        logger.info("Transform layer Engineering Started")
        logger.info("Transforming customers data")
        customer_df = transform_customers_data(customer_df)
        logger.info(f"No of customers after transformation: {len(customer_df)}")

        logger.info("Transforming Products Data")
        products_df = transform_products_data(products_df)
        logger.info(f"No of products after transformation: {len(products_df)}")

        logger.info("Transforming Orders Data")
        orders_df = transform_orders_data(orders_df)
        logger.info(f"No of orders after transformation: {len(orders_df)}")

        logger.info("Transforming Sales Data")
        sales_df = transform_sales_data(sales_df)
        logger.info(f"No of sales after transformation: {len(sales_df)}")
        logger.info("Transform layer Engineering ended")

        #----------------- Load Layer Engineering------------------
        print("Load Layer Engineering started")
        con = create_conn()
         
        logger.info("Loading customers data into customers table")
        load_data(customer_df,"customers",con)

        logger.info("Loading products data into products table")
        load_data(products_df,"products",con)

        logger.info("Loading orders data into orders table")
        load_data(orders_df,"orders",con)

        logger.info("Loading sales data into sales table")
        load_data(sales_df,"sales",con)

        logger.info("Load layer Engineering ended")

        con.close()



        logger.info("ETL pipeline completed successfully")
        print("ETL pipeline completed successfully")
    except Exception as e:
        logger.error(f"ETL pipeline failed: {str(e)}")


if __name__ == "__main__":
    main()
    