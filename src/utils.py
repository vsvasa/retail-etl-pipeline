import logging
import os
import configparser


def setup_logger():
    log_path = "logs/etl.log"
    os.makedirs("logs",exist_ok = True)

    logging.basicConfig(
        filename = log_path,
        level = logging.INFO,
        format = "%(asctime)s - %(levelname)s - %(message)s",
       
    )
    return logging

def read_config():
    config = configparser.ConfigParser()
    config.read("config/config.ini")

    return config