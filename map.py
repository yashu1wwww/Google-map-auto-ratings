from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

option = webdriver.ChromeOptions()
option.add_experimental_option("debuggerAddress", "localhost:8080")
driver = webdriver.Chrome(options=option)
time.sleep(3)
driver.get("https://www.google.com/maps/@12.9531904,77.6142848,12z?entry=ttu")
time.sleep(3)
search_box = driver.find_element_by_name("q")
search_box.send_keys("Oxford, MS, America") #replace with which you want to do ratings
search_box.send_keys(Keys.RETURN)
time.sleep(6)
driver.find_element(By.CSS_SELECTOR, "#QA0Szd > div > div > div.w6VYqd > div:nth-child(2) > div > div.e07Vkf.kA9KIf > div > div > div:nth-child(3) > div > div > button:nth-child(2) > div.LRkQ2 > div.Gpq6kf.fontTitleSmall").click() #click on review button 
time.sleep(4)
driver.find_element(By.CSS_SELECTOR, "#QA0Szd > div > div > div.w6VYqd > div:nth-child(2) > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf > div.m6QErb.Hk4XGb.QoaCgb.KoSBEe.tLjsW > div > button > span > span").click() #click on write a review
time.sleep(5)
driver.maximize_window()
time.sleep(4)
driver.find_element(By.CSS_SELECTOR, "#kCvOeb > div.O51MUd > div.C1FYvf > div > div.HDUCif > div > div.Rgwf9b > span.jwzVle > span > div.VfPpkd-dgl2Hf-ppHlrf-sM5MNb > button > span.VfPpkd-kBDsod > svg").click() #click on posting publicity icon for bypass msg
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="kCvOeb"]/div[1]/div[3]/div/div[2]/div/div[5]/svg').click()#click on 5th star
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="c2"]').send_keys("amazing school with good education system") #send review comment
time.sleep(2)
driver.find_element(By.CSS_SELECTOR "#kCvOeb > div.bTLhlf > div > div.kEocrb > div > button > div.VfPpkd-RLmnJb").click() #click on post button
time.sleep(4)
