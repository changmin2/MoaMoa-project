from bs4 import BeautifulSoup      
import requests
import re

def crawling():

    url = 'http://www.ikpnews.net/'
    driver = requests.get(url)
    soup_1 = BeautifulSoup(driver.text, 'html.parser') 


    content_1 = soup_1.find('div','auto-article auto-db01').find_all('li')
    news_name =[]
    href_list =[]
    for i in content_1:

        newstring = re.sub(r'[0-9]+', '', i.get_text())
        news_name.append(newstring)
        href_list.append(i.find('a')['href'])


    return news_name,href_list
    