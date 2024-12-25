## Part-1 Initializing Github repo and Package structure.
1. create github repo and connect it to local folder.
2. setup.py => setup.py and findpackages()
3. src: It will be a one of package (contains __init__.py file in it that helps the find package to identify whether a particular folder is a package or not!) (__init__.py file created.)
-e . basically create the package every time we run req.txt file and from setup.py it automatically create this.


## Part-2
src - Package(main Package)
    *components*(It basically contains all the important processes)
        - data ingestion (all data reading process.)
        - data transformation (all data cleaning and transformation process)
        - model trainer (model training process)
        - model pusher(pushing model to cloud)(optional)
    *pipeline* 
        - train_pipeline
        - predict_pipeline

    - Logging
    - Exception
        sys library
            in sys exc_info() will tell on which line the exception has occurred clearly.


GCV Details:
Args:
    - model: The machine learning model (e.g., RandomForestRegressor()).
    - param_grid: Dictionary of hyperparameters to tune.
    - X_train: Features for training.
    - y_train: Target variable for training.
    - cv: Number of cross-validation folds (default=5).
    - n_jobs: Number of jobs to run in parallel (-1 uses all available CPUs).
    - verbose: Level of verbosity during GridSearchCV (default=1).
    - refit: Whether to refit the best model on the entire dataset (default=True).

