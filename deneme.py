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
browser =webdriver.Chrome(service=chrome_service, options=chrome_options)
browser.get("https://sonuc.ysk.gov.tr/sorgu")

#Ai= browser.find_element(By.XPATH,"//*[@id='headingOne']/a/h4/span[1]")
#Ai.click()
#AA=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[2]/div[2]/div/div/table[1]/tbody/tr[1]/td[1]")

#AA.text
#print(AA)
#sleep(50)


