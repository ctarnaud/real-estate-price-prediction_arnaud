from asyncio.windows_events import NULL
from importlib.resources import contents
from webbrowser import get
from googlesearch import search
import re
import json
import time
import requests
import pandas as pd
from pandas import DataFrame
import os as o
from bs4 import BeautifulSoup
from urllib.request import urlopen
import selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
# driver = webdriver.Chrome("data_acquisition/chromedriver.exe")
# driver.get("https://www.immoweb.be/en")

def get_data_propoerty(property_url):
    req = requests.get(property_url)
    soup = BeautifulSoup(req.text, "html.parser") 
    # text = str(req.content)
    # return text
    # return soup.prettify

    content = soup.find("script", {"type": "text/javascript"}).contents[0]
    content = content[content.find('{'): content.rfind(';')]
    load_json = json.loads(content)
    print(load_json)
    dictionary = {"id": load_json}
    return dictionary




    #remove everything which is before the first curling bracket
    #remove the final semi colon (;)
    #load the content into a json 
    #create a new dictionary with the relevant information from the json
    #return the new dictionary
    return NULL
    
result = get_data_propoerty("https://www.immoweb.be/en/classified/apartment/for-sale/gavere/9890/10146915")
print(result)
property_url = "https://www.immoweb.be/en/classified/apartment/for-sale/gavere/9890/10146915"
reqs = requests.get(property_url)
soup = BeautifulSoup(reqs.text, 'html.parser')

#saving all the data as a csv file 
property_urls = []
f = open("test1.txt", "w")
for link in soup.find_all("a"):
   link_list = link.get('href')
   print(link_list)
   f.write(link_list)
   f.write("\n")
f.close()





