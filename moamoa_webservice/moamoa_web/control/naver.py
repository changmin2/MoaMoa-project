from bs4 import BeautifulSoup
from selenium import webdriver
import time          
from selenium.webdriver.common.keys import Keys
import re
def kakao_crawling(start,end):

    chrome_path = "C:\chromedriver/chromedriver.exe"
    driver = webdriver.Chrome(chrome_path)

    url = 'https://m.map.kakao.com/'
    driver.get(url)
    #페이지가 열릴때까지 기다려줌
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="daumHead"]/div[1]/div/a/span').click( )
    driver.find_element_by_xpath('//*[@id="kakaoGnb"]/ul/li[2]/a').click( )
    element = driver.find_element_by_xpath('//*[@id="startQuery"]')
    driver.find_element_by_xpath('//*[@id="departSearchForm"]/div/button/span').click( )
    time.sleep(1)
    element = driver.find_element_by_xpath('//*[@id="startQuery"]')
    element.send_keys(start)
    element.send_keys(Keys.RETURN) 
    try:
        driver.find_element_by_xpath('//*[@id="addressList"]/li/div/a').click( )
    except:
        driver.find_element_by_xpath('//*[@id="placeList"]/li[1]/a[1]').click( )
    element = driver.find_element_by_xpath('//*[@id="endQuery"]')
    element.send_keys(end)
    element.send_keys(Keys.RETURN) 
    try:
        driver.find_element_by_xpath('//*[@id="addressList"]/li/div/a').click( )
    except:
        driver.find_element_by_xpath('//*[@id="placeList"]/li[1]/a[1]').click( )
    driver.find_element_by_xpath('//*[@id="routeSearchWrap"]/div[2]/fieldset/div[2]/a[1]').click( )
    html_1 = driver.page_source 
    soup_1 = BeautifulSoup(html_1, 'html.parser') 
    text = soup_1.find('span','txt_routeinfo')
    get_num = text.get_text()
    num = re.findall(r'\d+',get_num)
    return num[0]
    
