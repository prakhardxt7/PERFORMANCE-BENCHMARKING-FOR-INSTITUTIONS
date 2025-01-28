import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass




@dataclass  #we will be able to define
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts','train.csv')
    test_data_path: str=os.path.join('artifacts','test.csv')
    raw_data_path: str=os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig() # this will store all three variables.
    def initiate_data_ingestion(self):
        logging.info('Enter the data ingestion method or component!')
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            data_file_path = os.path.join(current_dir, "data", "stud.csv")

            # Reading the CSV file
            df = pd.read_csv(data_file_path)

            logging.info('Read the dataset as dataframe!')
            
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            
            logging.info('Train Test Split Initiated!')
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)
            
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info('Ingestion of data is completed!')
            
            return (self.ingestion_config.train_data_path,
                    self.ingestion_config.test_data_path,
            )
        except Exception as e:
            raise CustomException(e,sys)
        
        
        

    
   