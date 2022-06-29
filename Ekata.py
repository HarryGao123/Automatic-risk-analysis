#!/usr/bin/env python
# coding: utf-8

# In[6]:


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pyquery import PyQuery as pq
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
from pyquery import PyQuery as pq
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

# In[2]:


def Ekata_login():
    # Github credentials
    username = " "
    password = " "

    # initialize the Chrome driver
    driver = webdriver.Edge()

    # head to github login page
    driver.get("https://app.ekata.com/sign_in")
    
    # find username/email field and send the username itself to the input field
    driver.find_element_by_id("profile_email").send_keys(username)
    
    # find password input field and insert password as well
    driver.find_element_by_id("profile_password").send_keys(password)
    # click login button
    driver.find_element_by_name("button").click()
    
    return driver


# In[5]:


# IP
def Ekata_IP(driver, ip):
 
    # click identity review
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div[1]").click()
    
    try:
        # type in IP address
        driver.find_element(By.ID, "ip_address").send_keys(ip)
    except ElementNotInteractableException:
        ekata_driver.find_element(By.XPATH, '//*[@id="down-icon"]').click()
        # type in IP address
        driver.find_element(By.ID, "ip_address").send_keys(ip)

    # click review
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/div[2]/button[1]").click()

    # wait until it is shown
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div/div/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]")))

    # get location
    location = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div/div/div[3]/div[1]/div[2]/div[2]/div[1]/div[2]/div[2]").text

    # get connection type
    conn_type = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div/div/div[3]/div[1]/div[2]/div[2]/div[3]/div[2]/div[2]").text
    register_org = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div/div/div[3]/div[1]/div[2]/div[2]/div[4]/div[2]/div[2]").text
    
    # click clear
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/div[2]/button[2]").click()
    
    return location, conn_type, register_org, driver

 


# In[45]:


def Ekata_phone(driver, country, phone, first_name, family_name):
    
    # Country code
    country_dic = np.load('contry_dic.npy',allow_pickle='TRUE').item()
    country_code = country_dic[country]

    # click phone button
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div[2]").click()

    # wait until it is shown
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div[2]/form/div[1]/div/div/label/div/div/div[1]/label/div[1]/input")))

    # type country code
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/div[1]/div/div/label/div/div/div[1]/label/div[1]/input").send_keys(country_code)

    # type phone number
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/div[1]/div/div/label/div/input").send_keys(phone)
    
    # click search
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/div[2]/button[1]").click()
    
    try: 

        # wait until it is shown
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div[1]/div[1]/header")))

         # get html 
        html = driver.page_source
        doc = pq(html).text()

        # check name if it is in html
        if first_name in doc:
            if_first_name = True
        else:
            if_first_name = False

        if family_name in doc:
            if_family_name = True
        else:
            if_family_name = False
    
    except NoSuchElementException:
        
        if_first_name = False
        if_family_name = False
  
    # click clear
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/div[2]/button[2]").click()
      
    return driver, if_first_name, if_family_name

 

# In[53]:


def Ekata_email(driver, email):
   
    # click email button
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[1]/div/div[1]/div[3]').click()

    # type email 
    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(email)
    
    # click search
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/div[2]/button[1]").click()

    # wait until it is shown
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div/div[2]/div[1]")))

    # email if seen before
    text = driver.find_element(By.XPATH, "/html/body/div/div/div[3]/div[1]/div/div[2]/div/div[2]/div[3]/div[2]").text
    
    if text == 'Never seen online':
        if_email = False
    else:
        text = text.split(' ')[-1]
        text = parser.parse(text)
        if diff_month(datetime.date(datetime.now()), text) >= 1:
             if_email = True
        else:
            if_email = False

    # click clear
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/div[2]/button[2]").click()
    
    return driver, if_email

  

# In[59]:


def Ekata_address(driver, address, state, country, first_name, family_name):
   
    # click address button
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[1]/div[4]").click()

    # type address 
    driver.find_element(By.XPATH, '//*[@id="street"]').send_keys(address)
    
    # type state 
    driver.find_element(By.XPATH, '//*[@id="where"]').send_keys(state)
    
     # type country 
    driver.find_element(By.XPATH, '//*[@id="countryCode"]').send_keys(country)
    
    # type search
    driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/form/div[2]/button[1]').click()
    
    try: 

        # wait until it is shown
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[3]/div[1]/div/div[2]/div[1]/div[1]/header")))

         # get html 
        html = driver.page_source
        doc = pq(html).text()

        # check name if it is in html
        if first_name in doc:
            if_first_name = True
        else:
            if_first_name = False

        if family_name in doc:
            if_family_name = True
        else:
            if_family_name = False
    
    except NoSuchElementException:
        
        if_first_name = False
        if_family_name = False
            
    # click clear
    driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/form/div[2]/button[2]").click()
      
    return driver, if_first_name, if_family_name

 