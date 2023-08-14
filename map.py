from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import time
import random
import os

option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress", "localhost:8080")
driver = webdriver.Chrome(options=option)
time.sleep(3)
driver.get("https://www.google.com/maps/@12.9531904,77.6142848,12z?entry=ttu")
time.sleep(3)
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("sarvodaya boys school") #replace with your search place
search_box.send_keys(Keys.RETURN)
time.sleep(6)

driver.find_element(By.CSS_SELECTOR, "#QA0Szd > div > div > div.w6VYqd > div:nth-child(2) > div > div.e07Vkf.kA9KIf > div > div > div:nth-child(3) > div > div > button:nth-child(2) > div.LRkQ2 > div.Gpq6kf.fontTitleSmall").click() #click on review button 

time.sleep(4)

driver.find_element(By.CSS_SELECTOR, "#QA0Szd > div > div > div.w6VYqd > div:nth-child(2) > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf > div.m6QErb.Hk4XGb.QoaCgb.KoSBEe.tLjsW > div > button > span > span").click() #click on write a review

#After clicking on the "Write a review" button, the star option appears, but it appears in medium size. I've tried all possible methods to avoid clicking the star button. If this issue occurs, I will add the remaining part of the code. Alternatively, if you are familiar with it, you can fork the repository.

