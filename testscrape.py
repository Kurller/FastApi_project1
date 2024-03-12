from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def initialize_driver():
   driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
   driver.get('https://www.youtube.com/@TechWithTim')
   return driver

def search_for_keyword(driver):
    search = driver.find_element(By.NAME, 'search_query')
    search.send_keys('python')
    search.send_keys(Keys.RETURN)
    return driver

def extract_video_titles(driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//*[@id="video-title"]'))
    )
    videos = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
    titles = [video.text for video in videos]
    print("Video Titles:")
    print(titles)
    print("Number of Videos:", len(titles))

driver = initialize_driver()
driver = search_for_keyword(driver)
extract_video_titles(driver)
