import os
import pickle
from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Importing from your project pipeline
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

# Define the path to the CSV file
CSV_FILE_PATH = "artifacts/user_input.csv"

# Function to save data to a CSV file
def save_to_csv(data_dict):
    try:
        # Convert the input data dictionary to a DataFrame
        df = pd.DataFrame([data_dict])

        # If the file exists, append without header; otherwise, create a new file with the header
        if os.path.exists(CSV_FILE_PATH):
            df.to_csv(CSV_FILE_PATH, mode='a', index=False, header=False)
        else:
            df.to_csv(CSV_FILE_PATH, mode='w', index=False, header=True)
    except Exception as e:
        print(f"Error saving data to CSV: {e}")

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the prediction functionality
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            # Gather inputs from the user
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('race_ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(request.form.get('reading_score')),
                writing_score=float(request.form.get('writing_score'))
            )

            # Convert the custom data to a DataFrame
            pred_df = data.get_data_as_data_frame()

            # Debugging: Log the DataFrame for verification
            print(f"Input DataFrame:\n{pred_df}")

            # Instantiate and run the prediction pipeline
            predict_pipeline = PredictPipeline()
            results = predict_pipeline.predict(pred_df)

            # Prepare the data dictionary for saving
            input_data_with_prediction = {
                'gender': request.form.get('gender'),
                'race_ethnicity': request.form.get('race_ethnicity'),
                'parental_level_of_education': request.form.get('parental_level_of_education'),
                'lunch': request.form.get('lunch'),
                'test_preparation_course': request.form.get('test_preparation_course'),
                'reading_score': float(request.form.get('reading_score')),
                'writing_score': float(request.form.get('writing_score')),
                'predicted_label': round(results[0], 2)
            }

            # Save the input data and prediction to the CSV file
            save_to_csv(input_data_with_prediction)

            # Return the prediction result to the HTML template
            return render_template('home.html', result=round(results[0], 2))
        except Exception as e:
            print(f"Error occurred: {e}")  # Debugging: Print the error in the console
            return render_template('home.html', result="Error during prediction. Check the inputs!")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
