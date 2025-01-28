from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
import os
import logging
import pandas as pd
from src.utils import load_object
from src.logger import logging
import time


class ModelDrift:
    def __init__(self, drift_threshold=0.3):  # Threshold set to 30%
        self.drift_threshold = drift_threshold

    def check_drift(self, train_data, new_data):
        column_name = "writing_score"  # Static column for drift detection
        try:
            # Check if the column is numeric
            if not pd.api.types.is_numeric_dtype(train_data[column_name]):
                logging.error(f"Column '{column_name}' is not numeric. Drift check requires a numeric column.")
                raise ValueError(f"Column '{column_name}' must be numeric.")

            # Calculate means of the selected column
            train_mean = train_data[column_name].mean()
            new_mean = new_data[column_name].mean()

            # Calculate percentage change in mean
            percent_change = abs((new_mean - train_mean) / train_mean) * 100

            # Log and print mean values and percentage change
            logging.info(f"Train data mean: {train_mean:.4f}, New data mean: {new_mean:.4f}")
            logging.info(f"Percentage change in mean: {percent_change:.2f}%")
            print(f"Train data mean: {train_mean:.4f}, New data mean: {new_mean:.4f}")
            print(f"Percentage change in mean: {percent_change:.2f}%")

            # Check if percentage change exceeds threshold
            if percent_change > self.drift_threshold * 100:
                logging.info("Drift detected in data.")
                print("Drift detected in data.")
                return True
            else:
                logging.info("No significant drift detected in data.")
                print("No significant drift detected in data.")
                return False

        except Exception as e:
            logging.error(f"Error occurred while checking drift: {str(e)}", exc_info=True)
            raise e


# Main pipeline
def train_pipeline():
    try:
        logging.info("Starting the training pipeline.")

        # Step 1: Data Ingestion
        logging.info("Step 1: Starting Data Ingestion...")
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
        logging.info(f"Step 1 Completed: Data ingestion completed. Train data path: {train_data_path}")

        # Load train data for drift comparison
        train_data = pd.read_csv(train_data_path)

        # Step 2: Load synthetic data
        current_dir = os.path.dirname(os.path.abspath(__file__))
        drift_file_path = os.path.join(current_dir, "data", "synthetic_stud_data.csv")
        new_data = pd.read_csv(drift_file_path)

        # Step 3: Check for drift
        logging.info("Step 3: Checking for drift...")
        drift_checker = ModelDrift()

        if drift_checker.check_drift(train_data, new_data):
            logging.info("Data Drift detected. Proceeding with caution.")
        else:
            logging.info("No significant data drift detected. Proceeding as usual.")

        logging.info("Training pipeline completed successfully.")
        return "Drift Check Completed"

    except Exception as e:
        logging.error("Error occurred in the training pipeline.", exc_info=True)
        raise e


if __name__ == "__main__":
    result = train_pipeline()
    print(f"Pipeline completed: {result}")
