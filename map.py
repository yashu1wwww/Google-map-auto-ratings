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
time.sleep(3)
driver.get("https://www.google.com/maps/@12.9531904,77.6142848,12z?entry=ttu")
time.sleep(3)
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("sarvodaya boys school")
search_box.send_keys(Keys.RETURN)
time.sleep(6)

driver.find_element(By.CSS_SELECTOR, "#QA0Szd > div > div > div.w6VYqd > div:nth-child(2) > div > div.e07Vkf.kA9KIf > div > div > div:nth-child(3) > div > div > button:nth-child(2) > div.LRkQ2 > div.Gpq6kf.fontTitleSmall").click() #click on review button 

time.sleep(4)

driver.find_element(By.CSS_SELECTOR, "#QA0Szd > div > div > div.w6VYqd > div:nth-child(2) > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf > div.m6QErb.Hk4XGb.QoaCgb.KoSBEe.tLjsW > div > button > span > span").click() #click on write a review

wait = WebDriverWait(driver, 10)
star_button = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/c-wiz/div/div/div/c-wiz/div/div[1]/div[3]/div/div[2]/div/div[5]'))) #star element

actions = ActionChains(driver)
actions.move_to_element(star_button).perform()

star_button.click()

time.sleep(3)

driver.find_element(By.CSS_SELECTOR, "#c2").send_keys("nyc school") #replace with your word

time.sleep(3)

driver.find_element(By.CSS_SELECTOR, "#kCvOeb > div.bTLhlf > div > div.kEocrb > div > button > span").click() #post button click

time.sleep(7)
