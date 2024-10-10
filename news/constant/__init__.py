from pathlib import Path
import os
import sys

HOME: Path=Path.cwd()

"""
defining common constant
"""
ARTIFACT_DIR: Path = HOME/Path("Artifact")
DATA_DIR: Path = HOME/Path("Data")

"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""

DATA_INGESTION_DATABASE_NAME="News"
DATA_INGESTION_RSS_FILE_NAME="List_of_RSS.csv"
DATA_INGESTION_MODEL_TRAINING_TABLE_NAME="Model_Training"
DATA_INGESTION_PREDICTION_TABLE_NAME="Daily_Article"


if __name__=='__main__':
    pass