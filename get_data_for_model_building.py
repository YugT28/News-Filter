import feedparser
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
import os
import sys

from dotenv import load_dotenv
load_dotenv()
MYSQL_CONNECTION_STRING=os.getenv("MYSQL_CONNECTION_STRING")

from news.exception.exception import NewsException
from news.logger.logger import logging

from news.utils.utility import rss_extract,join_tags,parse_html_summary,get_data








logging.info("Data for Model Building Downloading")
#natural-disaster
natural_disaster=get_data("https://www.theguardian.com/environment/climate-crisis/rss","Natural Disaster")
logging.info("natural-disaster data downloaded")

#Positive / Uplifting
column_name=['title', 'link', 'summary', 'author', 'tags', 'Category']
positive_category=["Society",'Environment','Lifestyle','Science','Economics','Opinion','UK','World','Partners']
positive=pd.DataFrame(columns=column_name)
for i in positive_category:
    df_positive=get_data(f"https://www.positive.news/category/{i}/feed/","Positive Uplifting")
    positive=positive._append(df_positive,ignore_index=True)
logging.info("Positive / Uplifting data downloaded")



#Terrorism /  Protest / Political Unrest / Riot
tpr=[
    "https://rss.nytimes.com/services/xml/rss/nyt/Politics.xml",
    "https://www.theguardian.com/politics/terrorism/rss",
    "https://www.theguardian.com/world/protest/rss",
]
tpr_dataset=pd.DataFrame(columns=column_name)
for i in tpr:
    df_tpr=get_data(i,"Terrorism Protest Political Unrest Riot")
    tpr_dataset=tpr_dataset._append(df_tpr,ignore_index=True)

logging.info("Terrorism /  Protest / Political Unrest / Riot data downloaded")

#Other
# other=get_data("https://www.theguardian.com/uk/lifeandstyle/rss","Other") # give some errror so we ahve to perform it manually

def extra(x):
    return " ".join([i.text for i in BeautifulSoup(x,"html.parser").find_all('p')])

other=rss_extract("https://www.theguardian.com/uk/lifeandstyle/rss")
other['tags']=other['tags'].apply(join_tags)
other['summary']=other['summary'].apply(extra)
if other.duplicated().sum():
    other.drop_duplicates()
other['Category']="Other"

logging.info("other data downloaded")

dataset=pd.concat([natural_disaster,tpr_dataset,positive,other])

#uploading to MYSQL
logging.info("Start Adding to MYSQL as Model_Training Table ")
engine = create_engine(MYSQL_CONNECTION_STRING)
dataset.to_sql("Model_Training",engine)
logging.info("Success to add Model_Training Table ")


