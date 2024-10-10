import pandas as pd

from news.logger.logger import logging

from news.pipeline.prediction_pipeline import PredictionPipeline

logging.info("Initiate Prediction Pipeline")
pp=PredictionPipeline()
pred=pp.initiate_prediction_pipeline()
pd.DataFrame(pred).to_csv("output.csv")
logging.info("Close Prediction Pipeline")