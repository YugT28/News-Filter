import feedparser
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
import os
import sys


def extend(x):
    for i in j:
        if i[0] == x:
            return i[1]

def map_it(x,y):
    global j
    j=y
    return list(map(extend,x))

"""
Utlilty For Data Fetching from URL
"""

def rss_extract(url)->pd.DataFrame:
    li=['title','link','summary','author','tags']
    urls=[url]
    model_building_article=pd.DataFrame(columns=li)
    for z in urls:
        feed=feedparser.parse(z)
        for i in feed['entries']:
            data={}
            for j in li:
                data[j]=i.get(j,np.nan)
            model_building_article=model_building_article._append(data,ignore_index=True)
    return model_building_article


def join_tags(x):
    if type(x)==list:
        add_tags=[]
        for i in x:
            add_tags.append(i['term'])
        return " ".join(add_tags)
    else:
        return np.nan



#clean summary column
def parse_html_summary(x):
    if type(x)==float:
        return x
    elif x.startswith("<"):
        soup = BeautifulSoup(x, 'html.parser')
        paragraph = soup.p.text
        return paragraph
    else:
        return x

def get_data(url:str,category:str)->pd.DataFrame:
    #geting data from rss url
    to_add=rss_extract(url)
    #clean tags column
    to_add['tags']=to_add['tags'].apply(join_tags)
    #clean summary column contain html syntax
    to_add['summary']=to_add['summary'].apply(parse_html_summary)
    #check duplicate if contain any then remove them
    if to_add.duplicated().sum():
        to_add.drop_duplicates()
    #adding category to dataframe
    to_add['Category']=category
    #returning rss data into dataframe
    return to_add

