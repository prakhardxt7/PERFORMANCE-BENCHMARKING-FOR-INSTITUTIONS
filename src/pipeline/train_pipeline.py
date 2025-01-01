from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.logger import logging

def train_pipeline():
    try:
        logging.info("Starting the training pipeline.")

        # Data Ingestion
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
        logging.info(f"Data ingestion completed. Train data path: {train_data_path}, Test data path: {test_data_path}")

        # Data Transformation
        data_transformation = DataTransformation()
        train_array, test_array,_ = data_transformation.initiate_data_transformation(train_data_path, test_data_path)
        logging.info("Data transformation completed.")

        # Model Training
        model_trainer = ModelTrainer()
        best_model_name, r2_square = model_trainer.initiate_model_trainer(train_array, test_array)
        logging.info(f"Model training completed. Best model: {best_model_name}, R2 Score: {r2_square}")

        logging.info("Training pipeline completed successfully.")

        return best_model_name, r2_square

    except Exception as e:
        logging.error("Error occurred in the training pipeline.", exc_info=True)
        raise e

if __name__ == "__main__":
    result = train_pipeline()
    print(f"Pipeline completed. Best Model: {result[0]}, R2 Score: {result[1]}")
