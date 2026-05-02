import logging
import os
from datetime import datetime

LOG_DIR = "logs"

def setup_logger():
    logger = logging.getLogger("loggerProject")

    if not logger.handlers:
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(filename)s::%(funcName)s - %(message)s"
        )

        os.makedirs(LOG_DIR, exist_ok=True)

        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        file_handler = logging.FileHandler(os.path.join(LOG_DIR, f"app_{timestamp}.log"))
        file_handler.setFormatter(formatter)

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger