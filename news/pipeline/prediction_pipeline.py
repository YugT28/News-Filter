import os
import sys
import pandas as pd

from news.exception.exception import NewsException
from news.logger.logger import logging

from news.component.data_ingestion import DataIngestion
from news.component.data_preprocessing import DataPreparation
from news.component.batch_prediction import BatchPrediction
from news.pipeline.training_pipeline import TrainingPipeline

from sqlalchemy import create_engine



engine=create_engine('mysql://root:root@localhost:3306/news')
class PredictionPipeline:
    def __init__(self):
        pass

    def initiate_prediction_pipeline(self):
        training_pipeline=TrainingPipeline()
        ett,data_model_dict=training_pipeline.initiate_training()
        estimator=ett['estimator']
        # estimator=ett['training']
        # estimator=ett['testing']
        transformer=data_model_dict['preprocessing_model'][0]
        encoder=data_model_dict['preprocessing_model'][1]

        #data_ingestion
        logging.info("data ingestion strated")
        data_ingestion = DataIngestion(engine)
        dataset = data_ingestion.load_data_for_prediction()
        logging.info("data ingestion ended")

        #data preprocessing
        logging.info("data prepration is started")
        data_preparation=DataPreparation()
        de=data_model_dict=data_preparation.preprocessing_for_prediction(dataset,transformer,encoder)
        logging.info("data prepration ended")

        #prediction
        logging.info("prediction started")
        batch_prediction=BatchPrediction()
        pred=batch_prediction.batch_prediction(de,estimator=estimator)
        logging.info("prediction ended")

        return pred



