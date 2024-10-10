import os
import sys
import pandas as pd

from news.exception.exception import NewsException
from news.logger.logger import logging


from sklearn.metrics import accuracy_score, classification_report


class ModelTraining:
    def __init__(self):
        pass

    def model_training(self, preprocessed, estimator):
        try:
            # data
            X_train = preprocessed['data'][0]
            X_test = preprocessed['data'][1]
            y_train = preprocessed['data'][2]
            y_test = preprocessed['data'][3]

            # training model
            estimator.fit(X_train, y_train)

            # testing with train data
            y_pred_train = estimator.predict(X_train)
            y_pred_test = estimator.predict(X_test)

            # evaluating training data
            training_accuracy = accuracy_score(y_train, y_pred_train)
            training_classification_report = classification_report(y_train, y_pred_train)

            # evaluating testing data
            testing_accuracy = accuracy_score(y_test, y_pred_test)
            testing_classification_report = classification_report(y_test, y_pred_test)

            return {'estimator': estimator,
                    'training': [training_accuracy, training_classification_report],
                    'testing': [testing_accuracy, testing_classification_report]
                    }
        except Exception as e:
            raise NewsException(e, sys)
