from bs4 import BeautifulSoup      
import requests

def policy():


    url = 'https://www.nongmin.com/news/NEWS/POL'
    driver = requests.get(url)
    soup_1 = BeautifulSoup(driver.text, 'html.parser') 


    content_1 = soup_1.find('div','news-section').find_all('li')

    news_name =[]
    href_list =[]
    for i in content_1:
        news_name.append(i.get_text())
        href_list.append(i.find('a')['href'])

    return news_name,href_list
