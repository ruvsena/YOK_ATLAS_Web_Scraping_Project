import selenium.webdriver as webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
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
browser.get("https://yokatlas.yok.gov.tr/lisans.php?y=102210277")
sleep(3)
#https://yokatlas.yok.gov.tr/lisans.php?y=102210277
#https://www.google-analytics.com/j/collect?v=1&_v=j101&a=1227742768&t=pageview&_s=1&dl=https%3A%2F%2Fyokatlas.yok.gov.tr%2Flisans.php%3Fy%3D102210277&ul=tr-tr&de=UTF-8&dt=BO%C4%9EAZ%C4%B0%C3%87%C4%B0%20%C3%9CN%C4%B0VERS%C4%B0TES%C4%B0%20-%20Bilgisayar%20M%C3%BChendisli%C4%9Fi%20(102210277)%20%7C%20Y%C3%96K%20Lisans%20Atlas%C4%B1&sd=24-bit&sr=1536x864&vp=802x795&je=0&_u=AACAAEABAAAAACAAI~&jid=&gjid=&cid=1000923138.1687970139&tid=UA-74941122-1&_gid=465198898.1690540455&_slc=1&z=1706103106
#reklamı kapatma
#close_add=browser.find_element(By.XPATH,"/html/body/div[3]/div/span")
#close_add.click()
#sleep(3)


kaynak =browser.page_source
soup= BeautifulSoup(kaynak, "html.parser")

baslık=soup.find_all("div",attrs={"class":"panel panel-default"})
liste=[]

#tables =browser.find_element("class","panel-body")
#//*[@id="icerik_1000_1"]/table[1]/tbody/tr[1]/td[1]
#/html/body/div[2]/div[1]/div[7]/div/div[2]/div[2]/div/div/table[1]/tbody/tr[1]/td[1]
#/html/body/div[2]/div[1]/div[7]/div/div[2]/div[2]/div/div/table[1]/tbody/tr[2]/td[1]
#//*[@id="icerik_1000_1"]/table[1]/tbody/tr[1]/td[1]

#//*[@id="headingOne"]/a/h4/span[2]
Ai= browser.find_element(By.XPATH,"//*[@id='headingOne']/a/h4/span[1]")
Ai.click()
AA= browser.find_elements(By.XPATH,"//*[@id='icerik_1000_1']/table[1]/thead/tr")
print(AA)
for metin in baslık:
    a =metin.find("h4",attrs={"class":"panel-title abaslik"})

    if a:
        k=a.text
        #print(k)
        liste.append([k])
for tablo in AA:
    if AA:
        AAv=AA.text
        print(AAv)
        liste.append([AAv])
db = pd.DataFrame(liste)
db.columns=["baslıklar"]
db.to_excel("makaleler.xlsx")

sleep(3000)

"""""""""
//*[@id="icerik_1000_1"]
//*[@id="icerik_1000_1"]/table[1]
//*[@id="icerik_1000_1"]/table[2]
//*[@id="icerik_1000_1"]/table[3]
"""