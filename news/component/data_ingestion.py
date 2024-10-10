import os
import sys
import pandas as pd

import feedparser
from sqlalchemy import create_engine,Column, String, Text
from sqlalchemy.orm import DeclarativeBase

from news.exception.exception import NewsException
from news.logger.logger import logging

from news.entity.config import DataIngestionConfig
from news.entity.artifact import DataIngestionArtifact

from news.constant import DATA_INGESTION_MODEL_TRAINING_TABLE_NAME,DATA_INGESTION_PREDICTION_TABLE_NAME

class DataIngestion:
    def __init__(self,engine):
        self.engine=engine

    def _load_data_from_database(self,table):
        try:
            query=f"select * from {table}"
            dataset = pd.read_sql(query, self.engine)
            dataset.reindex(dataset['index'])
            dataset.drop(columns=['index'], inplace=True)
            return dataset
        except Exception as e:
            raise NewsException(e,sys)

    def load_data_for_prediction(self):
        try:
            table=DATA_INGESTION_PREDICTION_TABLE_NAME
            return self._load_data_from_database(table)
        except Exception as e:
            raise NewsException(e,sys)
    def load_data_for_model_training(self):
        try:
            table=DATA_INGESTION_MODEL_TRAINING_TABLE_NAME
            return self._load_data_from_database(table)
        except Exception as e:
            raise NewsException(e,sys)

"""
# 
# class Base(DeclarativeBase):
#     pass

# class DataIngestion:
#     class News(Base):
#         __tablename__ = DATA_INGESTION_TABLE_NAME
#         link = Column(String(50), primary_key=True)
#         title = Column(Text)
#
#     def __init__(self,data_ingestion_config: DataIngestionConfig):
#         try:
#             self.data_ingestion_config = data_ingestion_config
#
#         except Exception as e:
#             raise NewsException(e)
#
#     def create_table(self):
#         connection_string = self.data_ingestion_config.connection_string
#         self.engine = create_engine(connection_string, echo=True)
#         Base.metadata.create_all(self.engine)
#
#
#     def create_table(self):
#
#     def fetch_data_from_url(self):
#         try:
#             list_of_rss=self.data_ingestion_config.list_of_rss
#
#             df = pd.read_csv(list_of_rss,header=None)
#
#             for i in df[0]:
#                 feed = feedparser.parse(i)
#                 if feed.get('bozo_exception', False):
#                     pass
#                 else:
#                     print("{}->{}".format(i, feed['bozo']))
#                     # print(feed.keys())
#                     print(feed['entries'][0].keys())
#
#             li = ['tags', 'title', 'summary', 'href', 'link', 'author']
#
#         except Exception as e:
#             raise NewsException(e,sys)
#
#     def segregate_data(self):
#         try:
#             pass
#         except Exception as e:
#             raise NewsException(e,sys)
#
#     def upload_data(self):
#         try:
#             pass
#         except Exception as e:
#             raise NewsException(e,sys)
#
#     def initiate_ingestion(self):
#         try:
#             pass
#         except Exception as e:
#             raise NewsException(e,sys)
#
"""






