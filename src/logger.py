#it is used for the purpose that any execution that probably happens we can able to capture/ log all the info, execution, every important info requires helps in tracking any error.
import logging
import os
from datetime import datetime



LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),'logs',LOG_FILE)
os.makedirs(logs_path,exist_ok=True)  #if directory already there so just keep appending the folder.

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)


logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


if __name__=='__main__':
    logging.info("Logging has started!")