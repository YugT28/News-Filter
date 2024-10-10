import os
import sys
import pandas as pd

from news.exception.exception import NewsException
from news.logger.logger import logging

from news.component.data_ingestion import DataIngestion
from news.component.data_preprocessing import DataPreparation
from news.component.model_training import ModelTraining

from sqlalchemy import create_engine

from sklearn.naive_bayes import MultinomialNB
from dotenv import load_dotenv
load_dotenv()
MYSQL_CONNECTION_STRING=os.getenv("MYSQL_CONNECTION_STRING")
class TrainingPipeline:
    def __init__(self):
        self.engine=create_engine(MYSQL_CONNECTION_STRING)

    def initiate_training(self):
        try:
            #data ingestion for model
            logging.info("data ingestion is started")
            data_ingestion=DataIngestion(self.engine)
            dataset=data_ingestion.load_data_for_model_training()
            logging.info("data ingestion ended")

            #data preprocessed
            logging.info("data prepration is started")
            data_preparation=DataPreparation()
            data_model_dict=data_preparation.preprocessing_for_model(dataset)
            logging.info("data prepration ended")

            #model training
            logging.info("model training started")
            model_training=ModelTraining()
            estimator = MultinomialNB()
            ett=model_training.model_training(data_model_dict,estimator=estimator)
            logging.info("Model training ended")

            # model=ett['estimator']
            # training_result=ett['training']
            # testing_result=ett['testing']
            return ett,data_model_dict
        except Exception as e:
            raise NewsException(e,sys)