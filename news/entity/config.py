import os
import sys
from datetime import datetime
from pathlib import Path


from news import constant

from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self,timestamp=datetime.now()):
        self.timestamp = timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.artifact_dir=constant.ARTIFACT_DIR/self.timestamp




class DataIngestionConfig(object):
    def __init__(self):
        self.connection_string=os.getenv('MYSQL_CONNECTION_STRING')
        self.list_of_rss=constant.HOME/constant.DATA_INGESTION_RSS_FILE_NAME
        self.table_name=constant.DATA_INGESTION_TABLE_NAME




