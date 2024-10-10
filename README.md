# Model Building 
***
1. Data we used for model building is webscraped from internet and not from Assignment.
2. Bit of Engineering is needed to get in form where data comes with label explicitly.
3. Use TFIDF to encode textual data.
4. Use Naive Bias to train model on that web scraped data.
5. Code all this with moduler coading 

# Prediction 
***
1. Use data provided in assignment in form of RSS
2. Add that data to MYSQL and adding link as primary key to avoid dublication.
3. Use TF-IDF for create embedding for Data.
4. Use trained model to predict category of given data

# Setup Project 
***
1. Clone Repo
```shell
git clone 
```
2. Create Enviornment
```shell
python -m venv .venv
```
3. Install All Dependencies
```shell
pip install -r requirements.txt
```
4. Create .env file and add
```text
MYSQL_CONNECTION_STRING=<--mysql connection string for MYSQL-->
```
```text
example:->
MYSQL_CONNECTION_STRING=mysql://root:root@localhost:3306/news
```
5. Start Data Ingestion From Given URL
```shell
python get_data_for_model_building.py
```
6. WebScraping For Model Development
```shell
python get_data_for_prediction.py
```

7. Train Model and Prediction on Fetched Data
```shell
python start_training.py
python start_prediction.py
```
### Check Output.csv for Prediction.

# Note
***
Need lots of improvement interms of ETL Data Ingestion , Model Building, Setting Up Training And Prediciton Schedule and ALL.

