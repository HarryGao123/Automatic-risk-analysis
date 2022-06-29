#!/usr/bin/env python
# coding: utf-8

# In[11]:

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pyquery import PyQuery as pq
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
from pyquery import PyQuery as pq
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.edge.options import Options 
import re
from bs4 import BeautifulSoup
from datetime import datetime
from dateutil import parser
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


def ip_proxy_login():
    
    name = ' '
    password = ' 
    
    url = 'https://www.ipqualityscore.com'
    options = Options()
    driver = webdriver.Edge(options=options)
    driver.get(url)

    # wait untile clickable
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="navbar-collapse-1"]/ul/li[7]/a')))
    button.click()

    # type login email
    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(name)

    # type password
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    
    # click login 
    driver.find_element(By.XPATH, '//*[@id="page-alt"]/section[1]/div/div/div/div/form[1]/div[3]/button').click()
    
    # wait
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/ul/li[2]/span')))

    # click Proxxy/Vpn Detection API
    driver.find_element(By.XPATH, '/html/body/div/div/ul/li[2]/span').click()

    # click Live Lookup
    driver.find_element(By.XPATH, '/html/body/div/div/ul/li[2]/ul/li[8]/a').click()
    
    return driver

def ip_proxy_check(driver, ip):
    
    # clear the initial ip
    driver.find_element(By.XPATH, '/html/body/main/section/div/div[2]/div[1]/form/div[1]/input').clear()

    # check ip
    driver.find_element(By.XPATH, '/html/body/main/section/div/div[2]/div[1]/form/div[1]/input').send_keys(ip, Keys.ENTER)
      
    # get html 
    html = driver.page_source
    doc = BeautifulSoup(html)
    
    text = doc.find('b', attrs={'class':'is_proxy'}).text
    
    if text == 'false':
        if_proxy = False
    else:
        if_proxy = True
        
    return driver, if_proxy

