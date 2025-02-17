import sys
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object


class PredictPipeline:
    def __init__(self):
        pass
    def predict(self,features):
        try:
            model_path='artifacts\model.pkl'
            preprocessor_path='artifacts\preprocessor.pkl'
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            data_scaled = preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        except Exception as e:
            raise CustomException(e,sys)   
     

class CustomData:  #it is responsible in mapping all the input data we give in html/or user input we can say
    def __init__(self,
                 gender: str,
                 group: str,
                 highest_qualification:str,
                 scholarship_eligibility:str,
                 standardized_test_preparation:str,
                 higher_education_performance:int,
                 high_school_performance: int):
        self.gender = gender
        self.group = group
        self.highest_qualification=highest_qualification
        self.scholarship_eligibility=scholarship_eligibility
        self.standardized_test_preparation=standardized_test_preparation
        self.higher_education_performance=higher_education_performance
        self.high_school_performance=high_school_performance
        #These values are basically coming from the web application,
        # we can check from home.html same variables and its components used or mapped(eg Gender is there and values are mapped is male and female)
    
    def get_data_as_data_frame(self): #this will return the entire inputs coming from a user in a data frame
        try:
            custom_data_input_dict={
                'gender':[self.gender],
                "group":[self.group],
                'highest_qualification':[self.highest_qualification],
                'scholarship_eligibility':[self.scholarship_eligibility],
                'standardized_test_preparation':[self.standardized_test_preparation],
                'higher_education_performance':[self.higher_education_performance],
                'high_school_performance':[self.high_school_performance]
            }
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e,sys)
        
        
            
         
        
        