from selenium import webdriver
import time
import pandas as pd
import os
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from app import database,models,Schemas
from app.models import Scrape
from sqlalchemy import create_engine
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def Linkedin_func():
    try:
        
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        Linkedin_home_page = driver.get('https://www.linkedin.com/')
        driver.implicitly_wait(3)
        # Get the username
        username = driver.find_element(By.XPATH, '//*[@id="session_key"]')
        # Get the password
        password = driver.find_element(By.XPATH, '//*[@id="session_password"]')
        # Get the login/submit button
        login = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')
        # Send login credentials to the form
        username.send_keys('kolaquadry@gmail.com')
        password.send_keys('Adebola@12345')
        login.click()
        time.sleep(3)
        driver.get("https://www.linkedin.com/jobs/collections/recommended/?currentJobId=3833638833&discoveryOrigin=JOBS_HOME_JYMBII")
        
        job_elements = driver.find_elements(By.CLASS_NAME, "base-card__full-link")
        
        
        
        # List to store job titles
        job_titles = []
        for job_element in job_elements:
            # Get text of each job element and append to job_titles list
            job_titles.append(job_element.text)
            # Print job element
        print(job_titles)
        print()
            #print(job_element.text)
            # Print total number of job titles
        print("Total number of jobs:", len(job_titles))
        company_elements = driver.find_elements(By.XPATH, '//h4/a')
        companyNames =[]
        for x in company_elements:
            companyNames.append(x.text)
        print(companyNames)
        print()
        print("total no of company :", len(companyNames))  
        loca_elements = driver.find_elements(By.CLASS_NAME, '//h4/a')
        locNames =[]
        for x in loca_elements:
            locNames.append(x.text)
        print(locNames)
        print()
        print("total no of company :", len(locNames))  
        companyfinal= pd.DataFrame(companyNames,columns=["companyNames"])
        titlefinal=pd.DataFrame(job_titles,columns=["job_titles"])
        final=companyfinal.join(titlefinal)
        
        print(final)
        #final.to_csv(r'C:\Users\kolawole\Downloads\archive\linkedinjob2.csv')
        engine = create_engine('postgresql://postgres:1234@localhost/Fastapi')
        final.to_sql('scrape_table',engine,if_exists='append',index=False)    
    except Exception as e:
           print(e)

Linkedin_func()
