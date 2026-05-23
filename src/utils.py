import logging
import os


def setup_logger():
    log_path = "logs/etl.log"
    os.makedirs("logs",exist_ok = True)

    logging.basicConfig(
        filename = log_path,
        level = logging.INFO,
        format = "%(asctime)s - %(levelname)s - %(message)s",
       
    )
    return logging