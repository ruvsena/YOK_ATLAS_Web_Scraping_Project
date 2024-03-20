import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from time import sleep
import pandas as pd
from bs4 import BeautifulSoup
from openpyxl import Workbook

user_agent ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
driver_path = r"C:\\Users\\pc\\Desktop\\chromedriver.exe"
chrome_service = Service(driver_path)
chrome_options = Options()
chrome_options.add_argument(f'user-agent={user_agent}')
driver =webdriver.Chrome(service=chrome_service, options=chrome_options)
# load website
url = 'https://angular.io/'

# get the entire website content
driver.get(url)

# select elements by class name
elements = driver.find_elements(By.CLASS_NAME, 'text-container')
for title in elements:
    # select H2s, within element, by tag name
    heading = title.find_element(By.TAG_NAME, 'h2').text
    # print H2s
    print(heading)
