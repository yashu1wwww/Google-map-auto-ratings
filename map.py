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
search_box.send_keys("Sarvodaya PU College, Tumakuru-1, Horpet, Ward No. 18, Tumkur, Tumakuru, Karnataka") #replace with your search place
search_box.send_keys(Keys.RETURN)

time.sleep(6)

driver.find_element(By.CSS_SELECTOR, "#QA0Szd > div > div > div.w6VYqd > div:nth-child(2) > div > div.e07Vkf.kA9KIf > div > div > div:nth-child(3) > div > div > button:nth-child(2) > div.LRkQ2 > div.Gpq6kf.fontTitleSmall").click() #click on review button 

time.sleep(4)

driver.find_element(By.CSS_SELECTOR, "#QA0Szd > div > div > div.w6VYqd > div:nth-child(2) > div > div.e07Vkf.kA9KIf > div > div > div.m6QErb.DxyBCb.kA9KIf.dS8AEf > div.m6QErb.Hk4XGb.QoaCgb.KoSBEe.tLjsW > div > button > span > span").click() #click on write a review

WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"/html/body/div[6]/iframe")))

time.sleep(2)

driver.find_element_by_css_selector("#kCvOeb > div.O51MUd > div.C1FYvf > div.NUTAPc.CbHt0b > div.HDUCif > div > div.Rgwf9b > span.jwzVle > span > div.VfPpkd-dgl2Hf-ppHlrf-sM5MNb > button > span.VfPpkd-kBDsod").click() #if popup appears...

time.sleep(1)

driver.find_element_by_xpath('/html/body/div/c-wiz/div/div/div/c-wiz/div/div[1]/div[3]/div/div[2]/div/div[5]').click() #click on 5 star 

time.sleep(2)

driver.find_element_by_xpath('/html/body/div/c-wiz/div/div/div/c-wiz/div/div[1]/div[3]/div/div[3]/div[1]/div/label/textarea').send_keys("amazing school") #comment about the place..

time.sleep(1)

driver.find_element_by_xpath('//*[@id="kCvOeb"]/div[2]/div/div[2]/div/button/span').click() #post button click

time.sleep(6)

#If You want using auto google acc login means use below 
#ADD These code in line 19th line by replace with that line...
#driver.get("https://accounts.google.com/v3/signin/identifier?authuser=0&continue=https%3A%2F%2Fwww.google.com%2Fmaps%2F%4012.9778041%2C77.5972793%2C17z%3Fentry%3Dttu&ec=GAlAcQ&hl=en&service=local&flowName=GlifWebSignIn&flowEntry=AddSession&dsh=S223320%3A1705299102932770&theme=glif")
#time.sleep(4)
#email=driver.find_element_by_id("identifierId")
#email.send_keys("myemail@gmail.com")
#email.send_keys(Keys.ENTER) #next button
#time.sleep(3)
#password=driver.find_element_by_name("Passwd")
#password.send_keys("password@123")
#password.send_keys(Keys.ENTER) #next button
#time.sleep(7)
