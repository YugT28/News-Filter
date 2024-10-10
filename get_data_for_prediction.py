import feedparser
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
import os
import sys

from news.exception.exception import NewsException
from news.logger.logger import logging

from dotenv import load_dotenv
load_dotenv()
MYSQL_CONNECTION_STRING=os.getenv("MYSQL_CONNECTION_STRING")

from news.utils.utility import rss_extract,join_tags,parse_html_summary,get_data

df=pd.read_csv("data/List_of_RSS.csv",header=None)
li=['title','link','summary','author','tags']

# pulling data
logging.info("Start adding data to daily_article")
daily_article=pd.DataFrame(columns=li)
for z in df[0]:
    feed=feedparser.parse(z)
    for i in feed['entries']:
        data={}
        for j in li:
            data[j]=i.get(j,np.nan)
        daily_article=daily_article._append(data,ignore_index=True)

# cleaning TAGS
daily_article['tags']=daily_article['tags'].apply(join_tags)

# cleaning Summary and parse its html containt
daily_article['summary']=daily_article['summary'].apply(parse_html_summary)

#uploading to MYSQL
engine = create_engine(MYSQL_CONNECTION_STRING)
daily_article.to_sql('daily_article',engine,if_exists='replace')
logging.info("End adding data to daily_article")