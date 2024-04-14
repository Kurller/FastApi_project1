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
        
        # Navigate to LinkedIn jobs page
        driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3897542940&f_TPR=r86400&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

        # Extract job titles, locations, and company names
        job_elements = driver.find_elements(By.CLASS_NAME, 'job-card-container__link')
        location_elements = driver.find_elements(By.CLASS_NAME, 'job-card-container__metadata-item')
        company_elements = driver.find_elements(By.CLASS_NAME, 'job-card-container__primary-description')

        company_names = []
        job_titles = []
        locations = []

        for job_element, location_element, company_element in zip(job_elements, location_elements, company_elements):
            job_titles.append(job_element.text)
            locations.append(location_element.text)
            company_names.append(company_element.text)

# Create DataFrames after accumulating the values
        companyfinal = pd.DataFrame(company_names, columns=["companyNames"])
        titlefinal = pd.DataFrame(job_titles, columns=["job_titles"])
        locationfinal = pd.DataFrame(locations, columns=['location'])

# Concatenate the DataFrames along the columns axis
        result = pd.concat([companyfinal, titlefinal, locationfinal], axis=1)
        print (result)
        #final.to_csv(r'C:\Users\kolawole\Downloads\archive\linkedinjob2.csv')
        engine = create_engine('postgresql://postgres:1234@localhost/Fastapi')
        result.to_sql('scrape',engine,if_exists='append',index=False)    
    except Exception as e:
           print(e)

Linkedin_func()
