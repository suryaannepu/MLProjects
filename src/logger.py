import logging
from datetime import datetime
import os

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
  filename=LOG_FILE_PATH,
  format="%(asctime)s - Line: %(lineno)d - Module: %(name)s - Level: %(levelname)s - Message: %(message)s",
  level=logging.INFO,


)

