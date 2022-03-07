from selenium import webdriver
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s=Service("C:/Users/Admin/AppData/Local/drivers/chromedriver.exe")

driver=webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com")
tit=driver.title
print(tit)
driver.find_element(By.ID, "txtUsername").send_keys("Admin")
#userName.send_keys("Admin")
passWord=driver.find_element(By.ID, "txtPassword").send_keys("admin123")
#passWord.send_keys("admin123")
driver.find_element_by_name("Submit").click()

#driver.close() //a
link=driver.find_element(By.CSS_SELECTOR, "a")
print(link)