import pandas as pd
from datetime import datetime

def get_last_loaded_date(tablename,connection):
    cur = connection.cursor()
    qry = "SELECT last_loaded_date FROM etl_metadata WHERE table_name = %s"
    cur.execute(qry, (tablename,))
    result = cur.fetchone()
    if result:
        return result[0]

    return None

def update_last_loaded_date(tablename,connection):
    cur = connection.cursor()
    currentdatetime = datetime.now()
    qry = """INSERT INTO etl_metadata (table_name, last_loaded_date) VALUES (%s, %s)
         ON DUPLICATE KEY UPDATE last_loaded_date = %s"""
    cur.execute(qry, (tablename, currentdatetime, currentdatetime))
    connection.commit()
    cur.close()


def filter_incremental_data(df, timestamp_column, last_loaded_timestamp):
    if last_loaded_timestamp is None:
        return df
    
    df[timestamp_column] = pd.to_datetime(df[timestamp_column])  # ✅ cast to datetime
    
    # Also ensure last_loaded_timestamp is datetime (defensive)
    if not isinstance(last_loaded_timestamp, datetime):
        last_loaded_timestamp = pd.to_datetime(last_loaded_timestamp)
    
    return df[df[timestamp_column] > last_loaded_timestamp]