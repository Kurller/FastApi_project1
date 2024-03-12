import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_path = r'C:\chromedriver.exe'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get('https://www.linkedin.com/')
time.sleep(3)

# Find and input username
username = driver.find_element(By.XPATH, '//*[@id="session_key"]')
username.send_keys('kolaquadry@gmail.com')

# Find and input password
password = driver.find_element(By.XPATH, '//*[@id="session_password"]')
password.send_keys('Adebola@12345')

# Find and click login button
login = driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')
login.click()

# Wait for the page to load
#time.sleep(5)

# Navigate to the job search page
driver.get("https://www.linkedin.com/jobs/collections/recommended/?currentJobId=3834670758&discoveryOrigin=JOBS_HOME_JYMBII")

# Wait for the search box to be clickable
#search = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "jobs-search-box__inner")))

# Clear the search box and input 'data analysts'
#search.clear()
#search.send_keys('data analysts')
#search.send_keys(Keys.RETURN)

# Wait for the main content to load
#main = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "main")))
#print(main)
