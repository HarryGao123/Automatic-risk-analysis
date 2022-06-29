#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[2]:


def Dossier_login(driver):

    # open dossier tab
    driver.execute_script("window.open('about:blank','dossier');")
    
    # switch to dossier
    driver.switch_to.window("dossier")

     # dossier login 
    driver.get("https://xcp.xboxlive.com/dossier")

    # click an account 
    driver.find_element(By.XPATH, '//*[@id="tilesHolder"]/div[1]/div/div').click()
    
    # wait 
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="DossierInput"]')))
    
    return driver


# In[3]:


def Dossier_check(driver, PUID, ip):
    
    Dossier_date = False
    Dossier_ip = False
    if_dossier=True
    
    # type PUID
    driver.find_element(By.XPATH, '//*[@id="DossierInput"]').send_keys(PUID, Keys.ENTER)
    
    if driver.find_element(By.XPATH, '/html/body/div/h2').text == 'Error':
        if_dossier = False
        driver.back()
        driver.refresh()
        return driver, Dossier_date, Dossier_ip, if_dossier
    
    else:
        
        # wait
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/a')))

        # get html 
        html = driver.page_source
        doc = BeautifulSoup(html)

        # get date
        date = doc.find('span', attrs={'class' : 'copyableText xboxOne copyableTextTitle'}).text.split(' - ')[0]
        date = parser.parse(date)

        if diff_month(datetime.today(), date) <= 30:
            Dossier_date = True
        else:
            Dossier_date = False

        if ip in doc.text:
            Dossier_ip = True
        else:
            Dossier_ip = False
            
        driver.back()
        driver.refresh()
    
    return driver, Dossier_date, Dossier_ip, if_dossier

