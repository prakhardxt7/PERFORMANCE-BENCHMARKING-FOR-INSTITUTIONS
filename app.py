import pickle
from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# Importing from your project pipeline
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)  # Initialize Flask app
app = application

# Route for the home page
@app.route('/')
def index():
    return render_template('index.html')  # Render the index.html template

# Route for the prediction functionality
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')  # Render the form for data input
    else:  # POST request - handle the form submission
        try:
            # Fetch data from the form and create a CustomData instance
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('race_ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(request.form.get('reading_score')),  # Converted to float
                writing_score=float(request.form.get('writing_score'))   # Converted to float
            )

            # Convert the custom data to a DataFrame
            pred_df = data.get_data_as_data_frame()

            # Debugging: Log the DataFrame for verification
            print(f"Input DataFrame:\n{pred_df}")  # This is for debugging

            # Instantiate and run the prediction pipeline
            predict_pipeline = PredictPipeline()  # Ensure PredictPipeline is correctly implemented
            results = predict_pipeline.predict(pred_df)

            # Return the prediction result to the HTML template
            return render_template('home.html', result=round(results[0], 2))  # Rounded to 2 decimal places
        except Exception as e:
            print(f"Error occurred: {e}")  # Debugging: Print the error in the console
            return render_template('home.html', result="Error during prediction. Check the inputs!")

if __name__ == "__main__":
    # Run the Flask app on localhost with debugging enabled
    app.run(host="127.0.0.1", port=5000, debug=True)
