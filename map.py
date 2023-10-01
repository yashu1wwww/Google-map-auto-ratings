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
option.add_experimental_option("debuggerAddress", "localhost:9222")
driver = webdriver.Chrome(options=option)
time.sleep(4)
driver.get("https://www.google.com/maps/@12.9531904,77.6142848,12z?entry=ttu")
time.sleep(4)
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("oxford school melbourne") #replace with your search place
search_box.send_keys(Keys.RETURN)

time.sleep(6)

driver.find_element(By.CSS_SELECTOR, "#QA0Szd > div > div > div.w6VYqd > div:nth-child(2) > div > div.e07Vkf.kA9KIf > div > div > div:nth-child(3) > div > div > button:nth-child(2) > div.LRkQ2 > div.Gpq6kf.fontTitleSmall").click() #click on review button 

time.sleep(4)

driver.find_element(By.CSS_SELECTOR, "#QA0Szd > div > div > div.w6VYqd > div:nth-child(2) > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf > div.m6QErb.Hk4XGb.QoaCgb.KoSBEe.tLjsW > div > button > span > span").click() #click on write a review

time.sleep(6)

driver.find_element_by_css_selector("#yDmH0d > c-wiz > div > div > div > div > div.O51MUd > div.l5dc7b > div.DTDhxc.eqAW0b > div.euWHWd.aUVumf > div > div:nth-child(5)").click() #click on rating button 

time.sleep(3)

driver.find_element_by_xpath('/html/body/div/c-wiz/div/div/div/c-wiz/div/div[1]/div[3]/div/div[3]/div[1]/div/label/textarea').send_keys("one of the best school") #comment about it

time.sleep(2)

driver.find_element_by_xpath('/html/body/div/c-wiz/div/div/div/c-wiz/div/div[2]/div/div[2]/div/button/div[1]').click() #click on post button

time.sleep(10)
