import datetime
import time
import re
import os
import csv
import pytz
from tzlocal import get_localzone
from bs4 import BeautifulSoup as Soup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

url = ("https://www.cevforbc.ca/")

hdr = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}


"""driver code (headless)"""
options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome('chromedriver.exe', options=options)
driver.get(url)

bs = Soup(driver.page_source, 'html.parser')

# close the chrome driver for less console time
driver.quit()

funds_container = bs.findAll("cufon", class_="cufon")

funds_remaining = int(re.sub(",", "", funds_container[1].get('alt')))
funds_reserved = int(re.sub(",", "", funds_container[3].get('alt')))
funds_disbursed = int(re.sub(",", "", funds_container[5].get('alt')))

# get current time
location = pytz.timezone('America/Los_Angeles')
current_time = datetime.datetime.now(tz=location)

current_time = current_time.replace(second=0, microsecond=0, tzinfo=None)

# check whether there already exists data
if os.path.isfile('./data.csv'):

    fields = [current_time,
              funds_remaining,
              funds_reserved,
              funds_disbursed]

    try:
        with open(r'data.csv', 'ab') as f:
            writer = csv.writer(f)
            writer.writerow(fields)
    except:
        pass

    print([current_time,
           funds_remaining,
           funds_reserved,
           funds_disbursed])

# if first time creating data.csv
else:
    headers = ['time', 'remaining', 'reserved', 'disbursed']

    try:
        with open(r'data.csv', 'wb') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            writer.writerow([current_time,
                             funds_remaining,
                             funds_reserved,
                             funds_disbursed])
    except:
        pass

    print([current_time,
           funds_remaining,
           funds_reserved,
           funds_disbursed])

# check whether file was opened
try:
    f
    f.close()
except:
    pass

