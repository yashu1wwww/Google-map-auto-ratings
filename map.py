import os
import time
import config
import numpy as np
import spintax
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from random import randint, randrange, random
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager as CM
from lxml.html import fromstring
import requests
from itertools import cycle
import json
import random

def login(email, password, proxy=None):

    options = uc.ChromeOptions()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-extensions")
    if proxy is not None:
        options.add_argument('--proxy-server=%s' % proxy)

    driver = uc.Chrome(options=options, executable_path=CM().install(),use_subprocess=True)
    driver.get('https://accounts.google.com/v3/signin/identifier?dsh=S-921757013%3A1687279134332255&continue=https%3A%2F%2Fwww.google.com%2Fmaps%2Fapi%2Fjs%2FReviewsService.CrossOriginAuthSuccess%3Fpb%3D%211shttps%253A%252F%252Fwww.google.com&hl=en&ifkv=Af_xneHefyDeZ1e-F6Dd2wIVUx4xfs5BV7hpPmSVEyNOoXkZ8PbI5xBYKNFi47JLLP-AzcLJX15APg&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

    wait=WebDriverWait(driver, 50);
    email_field=wait.until(EC.visibility_of_element_located((By.ID,'identifierId')))
    for char in email:
        email_field.send_keys(char)

    wait.until(EC.visibility_of_element_located((By.ID,"identifierNext"))).click()
    time.sleep(3)
    password_field=wait.until(EC.visibility_of_element_located((By.NAME,'Passwd')))
    for char in password:
        password_field.send_keys(char)
    wait.until(EC.visibility_of_element_located((By.ID,"passwordNext"))).click()
    
    time.sleep(3)#when accounts auto login if ask otp means change sleep into 15 seconds  
    
    with open("urls.txt") as f:
         for url in f:
             driver.get(url) 
             
    time.sleep(7)
    
    time.sleep(7)
    driver.find_element_by_xpath('/html/body/div[3]/div[9]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[3]/div[4]/div/button/span/div').click()
    #driver.implicitly_wait(7)
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/c-wiz/div/div/div/c-wiz/div/div[1]/div[3]/div/div[2]/div/div[5]/svg').click()
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div/c-wiz/div/div/div/c-wiz/div/div[1]/div[3]/div/div[3]/div[1]/div/label').send_keys("some text")
    #driver.find_element_by_css_selector('#kCvOeb > div.O51MUd > div.C1FYvf > div > div.G9Xzm > div.RAKQ3e.RNlq > div > label').send_keys("some text")
    time.sleep(5)
    driver.find_element_by_xpath('/html/body/div/c-wiz/div/div/div/c-wiz/div/div[2]/div/div[2]/div/button/div[1]').click()
    driver.find_element_by_css_selector('#kCvOeb > div.bTLhlf > div > div.kEocrb > div > button > div.VfPpkd-Jh9lGc').click()
    driver.close()#after one acc auto login and hits auto google ratings it again choose another accs and do same process


def main(email,password):
    driver = login(email, password)
    wait = WebDriverWait(driver, 50);
    keywords = [];
    
        
       

if __name__ == '__main__':
    with open('email.txt', 'r', encoding="utf8") as f:
        keywords = [line.strip() for line in f]
        for user in keywords:
            email_pass = user.split(",")
            main(email_pass[0],email_pass[1])

