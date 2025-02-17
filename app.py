import os
import pickle
from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

CSV_FILE_PATH = "artifacts/user_input.csv"

def save_to_csv(data_dict):
    try:
        df = pd.DataFrame([data_dict])
        if os.path.exists(CSV_FILE_PATH):
            df.to_csv(CSV_FILE_PATH, mode='a', index=False, header=False)
        else:
            df.to_csv(CSV_FILE_PATH, mode='w', index=False, header=True)
    except Exception as e:
        print(f"Error saving data to CSV: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predictdata', methods=['POST'])
def predict_datapoint():
    try:
        data = CustomData(
            gender=request.form.get('gender'),
            race_ethnicity=request.form.get('group'),
            parental_level_of_education=request.form.get('highest_qualification'),
            lunch=request.form.get('scholarship_eligibility'),
            test_preparation_course=request.form.get('standardized_test_preparation'),
            reading_score=float(request.form.get('higher_education_performance')),
            writing_score=float(request.form.get('high_school_performance'))
        )

        pred_df = data.get_data_as_data_frame()
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        input_data_with_prediction = {
            'gender': request.form.get('gender'),
            'group': request.form.get('group'),
            'highest_qualification': request.form.get('highest_qualification'),
            'scholarship_eligibility': request.form.get('scholarship_eligibility'),
            'standardized_test_preparation': request.form.get('standardized_test_preparation'),
            'higher_education_performance': float(request.form.get('higher_education_performance')),
            'high_school_performance': float(request.form.get('high_school_performance')),
            'predicted_label': round(results[0], 2)
        }

        save_to_csv(input_data_with_prediction)
        return render_template('index.html', result=round(results[0], 2))

    except Exception as e:
        print(f"Error occurred: {e}")
        return render_template('index.html', result="Error during prediction. Check inputs!")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
