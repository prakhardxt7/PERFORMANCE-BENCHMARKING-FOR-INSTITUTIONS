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
        
