import mysql.connector

from utils import read_config, setup_logger

logger = setup_logger()


def create_conn():

    try:
        config = read_config()
        conn = mysql.connector.connect(
            host=config['mysql']['host'],
            user=config['mysql']['user'],
            password=config['mysql']['password'],
            database=config['mysql']['database']
        )
        logger.info("Connection created successfully")
        return conn
    except Exception as e:
        logger.error(f"Error creating connection: {e}")
        return None


def load_data(df, table_name, connection):
    try:
        cur = connection.cursor()
        columns = ",".join(df.columns)
        placeholders = ",".join(["%s"] * len(df.columns))
        insertQry = f"""INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"""
        data = list(df.itertuples(index=False, name=None))
        batch_size = 50000
        for i in range(0, len(data), batch_size):
            batch = data[i:i + batch_size]
            cur.executemany(insertQry,batch)
            connection.commit()
            logger.info(f"Inserted rows {i} to {i + len(batch)} into {table_name}")
        logger.info(f"Loaded {len(df)} rows into {table_name}")
    except Exception as e:
        logger.error(f"Error loading data into {table_name}: {str(e)}")
        connection.rollback()
    finally:
        cur.close()