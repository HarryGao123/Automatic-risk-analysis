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


# In[2]:


def pay_load(driver, risk_guid):
    
     # open good_spend tab
    driver.execute_script("window.open('about:blank','good_spend');")
    
    # switch to good_spend
    driver.switch_to.window("good_spend")
    # url
    url = 'https://jarvisjx.cp.microsoft.com/probe/riskmod/?id='
    
    # type the risk_guid 
    driver.get(url+risk_guid)

    html = driver.page_source
    doc = pq(html).text()

    split_doc = doc.split(',')

    split_doc = set(split_doc)

    for i in split_doc:
        if 'd_AccountHistoricalBadGoodUSDRatio' in i:
            ratio = re.findall(r'\d+\.\d+', i) 

        if 'd_AccountHistoricalGoodUSD' in i:
            good_spend = re.findall(r'\d+\.\d+', i) 

        if 'd_AccountHistoricalBadUSD' in i:
            bad_spend = re.findall(r'\d+\.\d+', i) 
    
    driver.close()
            
    return ratio, good_spend, bad_spend

