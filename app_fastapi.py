from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
import pandas as pd
from src.pipeline.predict_pipeline import PredictPipeline, CustomData  # Import from the correct file path

app = FastAPI()

# Input model for prediction
class CustomDataInput(BaseModel):
    gender: str
    race_ethnicity: str
    parental_level_of_education: str
    lunch: str
    test_preparation_course: str
    reading_score: int
    writing_score: int

@app.get('/')
def index():
    return {'message': 'Welcome to the Student Performance Prediction API'}

@app.post('/predict')
def predict_student_performance(input_data: CustomDataInput):
    try:
        # Converting all inputs in a dataframe
        custom_data = CustomData(
            gender=input_data.gender,
            race_ethnicity=input_data.race_ethnicity,
            parental_level_of_education=input_data.parental_level_of_education,
            lunch=input_data.lunch,
            test_preparation_course=input_data.test_preparation_course,
            reading_score=input_data.reading_score,
            writing_score=input_data.writing_score
        )

        # dataframe
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
