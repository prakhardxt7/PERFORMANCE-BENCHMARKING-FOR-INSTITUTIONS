import os
import sys
from dataclasses import dataclass
import mlflow
import mlflow.sklearn

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor,
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_models
from datetime import datetime

@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts", "model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            # Set MLflow Tracking URI and experiment
            mlflow.set_tracking_uri("http://localhost:5001")  # URI for MLflow server
            mlflow.set_experiment("student_performance")

            logging.info("Split training and test input data")
            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:, -1],
                test_array[:, :-1],
                test_array[:, -1]
            )
            
            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                #"XGBRegressor": XGBRegressor(),
                #"CatBoosting Regressor": CatBoostRegressor(verbose=False),
                "AdaBoost Regressor": AdaBoostRegressor(),
            }

            params = {
                "Decision Tree": {
                    'criterion': ['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
                },
                "Random Forest": {
                    'n_estimators': [8, 16, 32, 64, 128, 256]
                },
                "Gradient Boosting": {
                    'learning_rate': [.1, .01, .05, .001],
                    'subsample': [0.6, 0.7, 0.75, 0.8, 0.85, 0.9],
                    'n_estimators': [8, 16, 32, 64, 128, 256]
                },
                "Linear Regression": {},
                "AdaBoost Regressor": {
                    'learning_rate': [.1, .01, 0.5, .001],
                    'n_estimators': [8, 16, 32, 64, 128, 256]
                }
            }

            model_report: dict = evaluate_models(
                X_train=X_train, y_train=y_train, X_test=X_test, y_test=y_test,
                models=models, param=params
            )

            # Log all models' results in MLflow
            for model_name, score in model_report.items():
                # Generate a run name based on model name and current timestamp
                run_name = f"{model_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
                with mlflow.start_run(run_name=run_name):
                    mlflow.log_param(f"{model_name}_score", score)
                    mlflow.log_param(f"{model_name}_params", str(params.get(model_name, {})))
                    print(f"Logged run for {model_name} with name: {run_name}")

            # To get best model score from dict
            best_model_score = max(sorted(model_report.values()))

            # To get best model name from dict
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException("No best model found")

            logging.info(f"Best found model on both training and testing dataset")

            # Log the best model details in MLflow
            with mlflow.start_run(run_name=f"Best_Model_{datetime.now().strftime('%Y%m%d_%H%M%S')}"):
                mlflow.log_param("best_model", best_model_name)
                mlflow.log_param("best_model_score", best_model_score)

                # Logging hyperparameters for the best model
                for param_name, param_value in params.get(best_model_name, {}).items():
                    mlflow.log_param(f"best_{param_name}", param_value)

                # Save the best model
                save_object(
                    file_path=self.model_trainer_config.trained_model_file_path,
                    obj=best_model
                )

                # Log the trained best model to MLflow (staging area)
                mlflow.sklearn.log_model(best_model, "best_model")

                predicted = best_model.predict(X_test)
                r2_square = r2_score(y_test, predicted)

                # Log the R² score as a metric for the best model
                mlflow.log_metric("best_r2_score", r2_square)

                print(f"Logged best model with name: Best_Model_{datetime.now().strftime('%Y%m%d_%H%M%S')}")

            # End the MLflow run
            mlflow.end_run()

            # Print process completion message
            print("Process completed. Model training and logging finished successfully.")

            return best_model_name, r2_square

        except Exception as e:
            print(f"Error occurred: {str(e)}")
            mlflow.end_run()
            raise CustomException(e, sys)
