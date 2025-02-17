from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pandas as pd
from src.pipeline.predict_pipeline import PredictPipeline, CustomData  # Import from the correct file path

app = FastAPI()

# Input model for prediction
class CustomDataInput(BaseModel):
    gender: str
    group: str
    highest_qualification: str
    scholarship_eligibility: str
    standardized_test_preparation: str
    higher_education_performance: int
    high_school_performance: int

@app.get('/')
def index():
    return {'message': 'Welcome to the Student Performance Prediction API'}

@app.post('/predict')
def predict_student_performance(input_data: CustomDataInput):
    try:
        # Converting all inputs in a dataframe
        custom_data = CustomData(
            gender=input_data.gender,
            group=input_data.group,
            highest_qualification=input_data.highest_qualification,
            scholarship_eligibility=input_data.scholarship_eligibility,
            standardized_test_preparation=input_data.standardized_test_preparation,
            higher_education_performance=input_data.higher_education_performance,
            high_school_performance=input_data.high_school_performance
        )

        # Convert to DataFrame
        input_df = custom_data.get_data_as_data_frame()

        # Initialize the prediction pipeline
        predict_pipeline = PredictPipeline()

        # Prediction using the pipeline
        prediction = predict_pipeline.predict(input_df)

        return {'Final_Score': prediction.tolist()}

    except Exception as e:
        return {'error': str(e)}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8080)