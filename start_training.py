from news.logger.logger import logging
from news.pipeline.training_pipeline import TrainingPipeline

logging.info("Initiate Model Training Pipeline")
tp=TrainingPipeline()
ett,data_model_dict=tp.initiate_training()
print(ett,data_model_dict)
logging.info("Close Model Training Pipeline")