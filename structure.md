ml-project/
|-- .git/                          # Git repository files
|-- .github/                       # GitHub workflows and actions
|   |-- workflows/                 # GitHub Actions workflows
|       |-- ci-cd.yml              # Continuous Integration/Continuous Deployment pipeline
|-- artifacts/                     # Model artifacts and preprocessed data
|   |-- model.pkl                  # Saved model file
|   |-- preprocessor.pkl           # Preprocessing pipeline file
|   |-- raw.csv                    # Raw dataset
|   |-- test.csv                   # Test dataset
|   |-- train.csv                  # Training dataset
|-- logs/                          # Logging directory
|-- ml_project.egg-info/           # Metadata for the project
|-- mlartifacts/                   # MLflow artifacts storage
|-- mlruns/                        # MLflow run logs
|   |-- .trash/                    # Deleted MLflow runs
|   |-- models/                    # Stored ML models
|-- notebook/                      # Jupyter Notebooks for exploration
|-- src/                           # Source code
|   |-- components/                # ML pipeline components
|       |-- data/                  # Data-related scripts
|       |-- __init__.py            # Package initialization
|       |-- data_ingestion.py      # Data ingestion module
|       |-- data_transformation.py # Data transformation module
|       |-- model_drift.py         # Model drift detection
|       |-- model_trainer.py       # Model training script
|       |-- model_trainer_main.py  # Main script for training
|   |-- pipeline/                  # Pipeline execution scripts
|   |-- __init__.py                # Package initialization
|   |-- exception.py               # Custom exceptions handling
|   |-- logger.py                  # Logging utility
|   |-- utils.py                   # Utility functions
|-- templates/                     # HTML templates for web app (if applicable)
|-- .gitignore                     # Git ignore file
|-- app_flask.py                   # Flask API script
|-- app.py                          # Main application script
|-- Dockerfile                      # Docker configuration
|-- eg_fast_api.txt                 # Example FastAPI script
|-- info.md                         # Project information
|-- README.md                       # Project documentation
|-- requirements.txt                 # Required dependencies
|-- setup.py                         # Package setup file