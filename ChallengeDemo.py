import requests
from requests.exceptions import MissingSchema, InvalidSchema, InvalidURL
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pytest
s=Service("C:/Users/Admin/AppData/Local/drivers/chromedriver.exe")
driver=webdriver.Chrome(service=s)

driver.get('http://develop.divercity.io/')
driver.maximize_window()
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
def links(var):

 footer= driver.find_element(By.XPATH, var)
 lists= footer.find_elements(By.CSS_SELECTOR,"a")
 print(len(lists))
 for link in lists:
    try:
         request = requests.head(link.get_attribute('href'), data={'key': 'value'})
         print("Status of " + link.get_attribute('href') + " is " + str(request.status_code))
    except requests.exceptions.InvalidSchema:
          print("InvalidSchema")


links("//*[@id='__next']/div/div[2]/footer/div/div[1]/div[2]/div[3]")#resources
links("//*[@id='__next']/div/div[2]/footer/div/div[1]/div[2]/div[2]")#company
links("//*[@id='__next']/div/div[2]/footer/div/div[1]/div[2]/div[1]")#prosucts&services
links("//*[@id='__next']/div/div[2]/footer/div/div[1]/div[2]/div[4]")#Connect
#footer_company = driver.find_element(By.XPATH, "//*[@id='__next']/div/div[2]/footer/div/div[1]/div[2]/div[2]").find_elements(By.CSS_SELECTOR,"a")


time.sleep(5)
driver.quit()



