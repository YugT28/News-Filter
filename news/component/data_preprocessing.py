import os
import sys
import pandas as pd

from news.exception.exception import NewsException
from news.logger.logger import logging




from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder



class DataPreparation:
    def __init__(self):
        pass

    def combine_dataset(self,dataset):
        try:
            combined = dataset['title'] + dataset['summary'] + dataset['tags'] + dataset['author']
            return combined
        except Exception as e:
            raise NewsException(e,sys)

    def transform_embedding_model(self,X):
        try:
            transformer=TfidfVectorizer(max_features=1000)
            transformer.fit(X)
            return transformer
        except Exception as e:
            raise NewsException(e,sys)
    def label_transformer(self,y):
        try:
            transformer=LabelEncoder()
            transformer.fit(y)
            return transformer
        except Exception as e:
            raise NewsException(e,sys)




    def preprocessing_for_model(self,dataset):
        try:
            combined=self.combine_dataset(dataset)
            total = pd.concat([combined, dataset['Category']], axis=1)

            #split data
            X = total[0]
            y = total['Category']

            #train test split
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

            #fill missing value
            X_train = X_train.fillna("AAA")
            X_test = X_test.fillna("AAA")

            #transform into vectoriser
            transformer = self.transform_embedding_model(X_train)
            X_train_transformed=transformer.transform(X_train)
            X_test_transformed=transformer.transform(X_test)

            #label Encoding
            encoder=self.label_transformer(y_train)
            y_train_transformed=encoder.transform(y_train)
            y_test_transformed = encoder.transform(y_test)

            return {'data':[X_train_transformed,X_test_transformed,y_train_transformed,y_test_transformed],
                    'preprocessing_model':[transformer,encoder]
                    }
        except Exception as e:
            raise NewsException(e,sys)


    def preprocessing_for_prediction(self,dataset:pd.DataFrame,transformer:TfidfVectorizer,encoder:LabelEncoder):
        try:
            #combine everything
            combined=self.combine_dataset(dataset)

            #fillna
            combined=combined.fillna("AAA")

            #transform into vectors
            combined=transformer.transform(combined)

            return {'data':combined,
                    'label_encoder':encoder
                    }
        except Exception as e:
            raise NewsException(e,sys)





