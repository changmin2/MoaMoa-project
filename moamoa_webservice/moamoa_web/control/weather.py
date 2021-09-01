from bs4 import BeautifulSoup      
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

import pandas  as pd   

def weather(location):
    url='https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={}+날씨'.format(location)
    driver=requests.get(url)
    soup = BeautifulSoup(driver.text,'html.parser')
    temp=soup.find('span','todaytemp').get_text()
    last = soup.find('div','info_data').find('ul','info_list').find('li').get_text()
    temp_min = soup.find('span','min').get_text()
    temp_max = soup.find('span','max').get_text()
    chegam  = soup.find('span','sensible').find('span','num').get_text()
    mise = soup.find('div','detail_box').get_text()

    return temp,last,temp_min,temp_max,chegam,mise

