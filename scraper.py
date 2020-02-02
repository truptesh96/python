# -*- coding: utf-8 -*-
"""
Webscraping script for Airquality Index

"""
# Importing Libraries
import requests
import os
import time

# Webscraper Function For getting data from website
def get_data():
    for year in range(2010,2012):
        os.mkdir('data/{}'.format(year))
        for month in range(1,13):
            if month < 10 :
                url = 'https://en.tutiempo.net/climate/0{}-{}/ws-426470.html'.format(month,year)
            else:
                url = 'https://en.tutiempo.net/climate/{}-{}/ws-426470.html'.format(month,year)
            page_html = requests.get(url).text
            encoded_html = page_html.encode('utf-8')
            f = open('data/{}/{}.html'.format(year,month),"wb+")
            f.write(encoded_html)
            f.close()

# Refine Data Function
from bs4 import BeautifulSoup
def refine_data():
    for year in range(2010,2012):
        

# For checking how much time script will take to perfom all operations            
if __name__ == '__main__':
    start_time = time.time()
    get_data()
    end_time = time.time()
    print('Time Taken for Scraping is:{} seconds'.format(end_time- start_time))