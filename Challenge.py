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
footer_resources= driver.find_element(By.XPATH, "//*[@id='__next']/div/div[2]/footer/div/div[1]/div[2]/div[3]").find_elements(By.CSS_SELECTOR,"a")
print(len(footer_resources))
for link in footer_resources:
#def links():
       try:
        request = requests.head(link.get_attribute('href'), data={'key': 'value'})
        print("Status of " + link.get_attribute('href') + " is " + str(request.status_code))
        if(request.status_code >= 400) and (request.status_code < 500):
            print("Broken link")
       except requests.exceptions.MissingSchema:
         print("Broken")
footer_company = driver.find_element(By.XPATH, "//*[@id='__next']/div/div[2]/footer/div/div[1]/div[2]/div[2]").find_elements(By.CSS_SELECTOR,"a")
print(len(footer_company))
for link in footer_company:
       try:
        request = requests.head(link.get_attribute('href'), data={'key': 'value'})
        print("Status of " + link.get_attribute('href') + " is " + str(request.status_code))
       except requests.exceptions.MissingSchema:
         print("Broken")
#footer_Connect = driver.find_element(By.XPATH,"//*[@id='__next']/div/div[2]/footer/div/div[1]/div[2]/div[4]").find_elements(By.CSS_SELECTOR,"a")
#print(len(footer_Connect))
#for link in footer_Connect:
    #   try:
     #    request = requests.head(link.get_attribute('href'), data={'key': 'value'})
       #  print("Status of " + link.get_attribute('href') + " is " + str(request.status_code))
      # except requests.exceptions.MissingSchema:
      #   print("Broken")
footer_Product = driver.find_element(By.XPATH,"//*[@id='__next']/div/div[2]/footer/div/div[1]/div[2]/div[1]").find_elements(By.CSS_SELECTOR,"a")
print(len(footer_Product))
for link in footer_Product:
    try:
        request = requests.head(link.get_attribute('href'), data={'key': 'value'})
        print("Status of " + link.get_attribute('href') + " is " + str(request.status_code))
    except requests.exceptions.MissingSchema:
         print("Broken")
time.sleep(5)
driver.quit()



