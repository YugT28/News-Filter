# Model Building 
***
1. Data we used for model building is webscraped from internet.
2. This data comes with label explicitly. Bit of Engineering is needed to get in that form
3. Use Naive Bias to train model on that web scraped data.
4. Code all this with moduler coading 

# Prediction 
***
1. Use data provided in assignment
2. Use trained model to predict category of given data
3. Use TF-IDF for create embedding for Data.

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

