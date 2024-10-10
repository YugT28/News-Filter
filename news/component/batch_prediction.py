import os
import sys
import pandas as pd

from news.exception.exception import NewsException
from news.logger.logger import logging

from news.utils.utility import map_it


class BatchPrediction:
    def __init__(self):
        pass
    def batch_prediction(self, pred_preprocessed, estimator):
        try:
            dataset = pred_preprocessed['data']
            label_encoder = pred_preprocessed['label_encoder']

            #prediction in numeric
            pred = estimator.predict(dataset)

            #interpret in categorical
            labels = list(enumerate(label_encoder.classes_))
            return map_it(pred,labels)
        except Exception as e:
            raise NewsException(e, sys)

