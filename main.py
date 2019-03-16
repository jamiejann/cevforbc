import datetime
import re
import os
import csv
from bs4 import BeautifulSoup as Soup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = ("https://www.cevforbc.ca/")

"""driver code (headless)"""
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome('C:/Users/jami/Desktop/master/chromedriver.exe', options=options)
driver.get(url)

bs = Soup(driver.page_source, 'html.parser')
funds_container = bs.findAll("cufon", class_="cufon")

funds_remaining = re.sub(",", "", funds_container[1].get('alt'))
funds_reserved = re.sub(",", "", funds_container[3].get('alt'))
funds_disbursed = re.sub(",", "", funds_container[5].get('alt'))

# get current time
current_time = datetime.datetime.now()

if os.path.isfile('./data.csv'):

    fields = [current_time,
              funds_remaining,
              funds_reserved,
              funds_disbursed]

    with open(r'data.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(fields)
else:

    headers = ['time', 'remaining', 'reserved', 'disbursed']

    with open('data.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerow([current_time,
                         funds_remaining,
                         funds_reserved,
                         funds_disbursed])

f.close()
