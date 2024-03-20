
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


first_column=[]
iki=[]
uc=[]
dort=[]
bes=[]
altı=[]
yedi=[]
sekiz=[]
dokuz=[]

def bos_bırak():
    uc.append(" ")
    iki.append(" ")
    dort.append(" ")
    bes.append(" ")
    altı.append(" ")
    yedi.append(" ")
    sekiz.append(" ")
    dokuz.append(" ")

user_agent ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.5993.70 Safari/537.36'
driver_path = r"C:\\Users\\pc\\Desktop\\chromedriver.exe"
chrome_service = Service(driver_path)
chrome_options = Options()
chrome_options.add_argument(f'user-agent={user_agent}')
browser =webdriver.Chrome(service=chrome_service, options=chrome_options)
browser.get("https://yokatlas.yok.gov.tr/lisans.php?y=102210277")

wait = WebDriverWait(browser, 60)
wait1 = WebDriverWait(browser,1)

sleep(3)
elements = browser.find_elements(By.CLASS_NAME, 'accordion-toggle')
"""""
for title in elements:
	heading = title.find_element(By.TAG_NAME, 'h4')
	print(heading.text)
"""""""""
b1=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[2]/div[1]/a/h4")
print(b1.text)
first_column.append(b1.text)
b1.click()
bos_bırak()

k = wait.until(EC.presence_of_all_elements_located(
    (By.XPATH, "/html/body/div[2]/div[1]/div[7]/div/div[2]/div[2]/div/div/table[1]/thead/tr/th/big")))
print([i.text for i in k])
iki.append(str([i.text for i in k]))
first_column.append("")
uc.append(" ")
dort.append(" ")
bes.append(" ")
altı.append(" ")
yedi.append(" ")
sekiz.append(" ")
dokuz.append(" ")

for sayi in range(1,7):
   tablo = wait.until(EC.presence_of_all_elements_located(
           (By.XPATH, "/html/body/div[2]/div[1]/div[7]/div/div[2]/div[2]/div/div/table[1]/tbody/tr["+ str(sayi) +"]/td[1]")))
   tablo1 = wait.until(EC.presence_of_all_elements_located(
           (By.XPATH,
        "/html/body/div[2]/div[1]/div[7]/div/div[2]/div[2]/div/div/table[1]/tbody/tr[" + str(sayi) + "]/td[2]")))
   print([i.text for i in tablo],[i.text for i in tablo1])
   first_column.append("")
   iki.append(str([i.text for i in tablo]))
   uc.append(str([i.text for i in tablo1]))
   dort.append(" ")
   bes.append(" ")
   altı.append(" ")
   yedi.append(" ")
   sekiz.append(" ")
   dokuz.append(" ")

for sayi in range(1, 11):
   tablo2 = wait.until(EC.presence_of_all_elements_located(
       (By.XPATH,
        "/html/body/div[2]/div[1]/div[7]/div/div[2]/div[2]/div/div/table[2]/tbody/tr[" + str(sayi) + "]/td[1]")))
   tablo21 = wait.until(EC.presence_of_all_elements_located(
       (By.XPATH,
        "/html/body/div[2]/div[1]/div[7]/div/div[2]/div[2]/div/div/table[2]/tbody/tr[" + str(sayi) + "]/td[2]")))
   print([i.text for i in tablo2], [i.text for i in tablo21])
   first_column.append("")
   iki.append(str([i.text for i in tablo2]))
   uc.append(str([i.text for i in tablo21]))
   dort.append(" ")
   bes.append(" ")
   altı.append(" ")
   yedi.append(" ")
   sekiz.append(" ")
   dokuz.append(" ")
for sayi in range(1, 10):
   tablo3 = wait.until(EC.presence_of_all_elements_located(
       (By.XPATH,
        "/html/body/div[2]/div[1]/div[7]/div/div[2]/div[2]/div/div/table[3]/tbody/tr[" + str(sayi) + "]/td[1]")))
   tablo31 = wait.until(EC.presence_of_all_elements_located(
       (By.XPATH,
        "/html/body/div[2]/div[1]/div[7]/div/div[2]/div[2]/div/div/table[3]/tbody/tr[" + str(sayi) + "]/td[2]")))
   print([i.text for i in tablo3], [i.text for i in tablo31])
   first_column.append("")
   iki.append(str([i.text for i in tablo3]))
   uc.append(str([i.text for i in tablo31]))
   dort.append(" ")
   bes.append(" ")
   altı.append(" ")
   yedi.append(" ")
   sekiz.append(" ")
   dokuz.append(" ")
####
b2=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[3]/div[1]/a")
print(b2.text)
b2.click()
first_column.append(str(b2.text))
bos_bırak()

s3=1
s4=1
for k in range(1,7):
    t1 = wait.until(EC.presence_of_all_elements_located(
        (By.XPATH,
         "/html/body/div[2]/div[1]/div[7]/div/div[3]/div[2]/div/div/table/thead/tr[1]/th["+str(k)+"]")))

    t2 = wait.until(EC.presence_of_all_elements_located(
        (By.XPATH,
         "/html/body/div[2]/div[1]/div[7]/div/div[3]/div[2]/div/div/table/tbody/tr[1]/td["+str(k)+"]")))
    t3,t4=[],[]
    if s3==1 or s3== 2:
        t3 = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "/html/body/div[2]/div[1]/div[7]/div/div[3]/div[2]/div/div/table/tbody/tr[2]/td[" + str(s3) + "]")))
        t4 = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[3]/div[2]/div/div/table/tbody/tr[3]/td[" + str(s3) + "]")))

    s3=s3+0.5
    if s3>=3:
        s3=3

    t5,t6 = [],[]
    if s4 == 1or s4 ==2 or s4 ==3:
        t5 = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[3]/div[2]/div/div/table/tbody/tr[4]/td[" + str(s4) + "]")))
        t6 = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[3]/div[2]/div/div/table/tbody/tr[5]/td[" + str(s4) + "]")))

    s4=s4+1
    if s4 >= 4:
        s4=4

    print([i.text for i in t1], [i.text for i in t2],[i.text for i in t3],[i.text for i in t4],[i.text for i in t5],[i.text for i in t6])
    first_column.append("")
    iki.append(str([i.text for i in t1]))
    uc.append(str([i.text for i in t2]))
    dort.append(str([i.text for i in t3]))
    bes.append(str([i.text for i in t4]))
    altı.append(str([i.text for i in t5]))
    yedi.append(str([i.text for i in t6]))
    sekiz.append(" ")
    dokuz.append(" ")

####
b3=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[4]/div[1]/a/h4")
print(b3.text)
b3.click()
first_column.append(str(b3.text))
bos_bırak()

for c in range(1,4):
    c1 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[4]/div[2]/div/div/table/thead/tr/th["+str(c)+"]")))
    c2= wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[4]/div[2]/div/div/table/tbody/tr[1]/td["+str(c)+"]")))
    c3 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[4]/div[2]/div/div/table/tbody/tr[2]/td["+str(c)+"]")))
    print([i.text for i in c1],[i.text for i in c2],[i.text for i in c3])
    first_column.append("")
    iki.append(str([i.text for i in c1]))
    uc.append(str([i.text for i in c2]))
    dort.append(str([i.text for i in c3]))
    bes.append(" ")
    altı.append(" ")
    yedi.append(" ")
    sekiz.append(" ")
    dokuz.append(" ")
#####
b4=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[5]/div[1]/a/h4")
print(b4.text)
b4.click()
first_column.append(str(b4.text))
bos_bırak()

for c in range(1,5):
    c1 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[5]/div[2]/div/div/table[1]/thead/tr/th["+str(c)+"]")))
    c2= wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[5]/div[2]/div/div/table[1]/tbody/tr[1]/td["+str(c)+"]")))
    c3 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[5]/div[2]/div/div/table[1]/tbody/tr[2]/td["+str(c)+"]")))
    c4 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[5]/div[2]/div/div/table[1]/tbody/tr[3]/td["+str(c) + "]")))
    print([i.text for i in c1],[i.text for i in c2],[i.text for i in c3],[i.text for i in c4])
    first_column.append("")
    iki.append(str([i.text for i in c1]))
    uc.append(str([i.text for i in c2]))
    dort.append(str([i.text for i in c3]))
    bes.append(str([i.text for i in c4]))
    altı.append(" ")
    yedi.append(" ")
    sekiz.append(" ")
    dokuz.append(" ")
for c in range(1,4):
    c1 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[5]/div[2]/div/div/table[2]/thead/tr/th["+str(c)+"]")))
    c2= wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[5]/div[2]/div/div/table[2]/tbody/tr[1]/td["+str(c)+"]")))
    c3 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[5]/div[2]/div/div/table[2]/tbody/tr[2]/td["+str(c)+"]")))
    c4 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH, "/html/body/div[2]/div[1]/div[7]/div/div[5]/div[2]/div/div/table[2]/tbody/tr[3]/td[" + str(c) + "]")))
    c5 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH, "/html/body/div[2]/div[1]/div[7]/div/div[5]/div[2]/div/div/table[2]/tbody/tr[4]/td[" + str(c) + "]")))
    print([i.text for i in c1],[i.text for i in c2],[i.text for i in c3],[i.text for i in c4],[i.text for i in c5])
    first_column.append("")
    iki.append(str([i.text for i in c1]))
    uc.append(str([i.text for i in c2]))
    dort.append(str([i.text for i in c3]))
    bes.append(str([i.text for i in c4]))
    altı.append(str([i.text for i in c5]))
    yedi.append( " ")
    sekiz.append(" ")
    dokuz.append(" ")
####
b5=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[6]/div[1]/a/h4")
print(b5.text)
b5.click()
first_column.append(str(b5.text))
bos_bırak()

for c in range(1,4):
    c1 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[6]/div[2]/div/div/table/thead/tr/th["+str(c)+"]")))
    c2= wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[6]/div[2]/div/div/table/tbody/tr[1]/td["+str(c)+"]")))
    c3 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[6]/div[2]/div/div/table/tbody/tr[2]/td["+str(c)+"]")))
    c4 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[6]/div[2]/div/div/table/tbody/tr[3]/td["+str(c)+"]")))
    c5 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[6]/div[2]/div/div/table/tbody/tr[4]/td["+str(c)+"]")))
    c6 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[6]/div[2]/div/div/table/tbody/tr[5]/td["+str(c)+"]")))
    c7 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[6]/div[2]/div/div/table/tbody/tr[6]/td["+str(c)+"]")))
    c8 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[6]/div[2]/div/div/table/tbody/tr[7]/td["+str(c)+"]")))
    print([i.text for i in c1], [i.text for i in c2], [i.text for i in c3], [i.text for i in c4], [i.text for i in c5], [i.text for i in c6], [i.text for i in c7], [i.text for i in c8])
    first_column.append("")
    iki.append(str([i.text for i in c1]))
    uc.append(str([i.text for i in c2]))
    dort.append(str([i.text for i in c3]))
    bes.append(str([i.text for i in c4]))
    altı.append(str([i.text for i in c5]))
    yedi.append(str([i.text for i in c6]))
    sekiz.append(str([i.text for i in c7]))
    dokuz.append(str([i.text for i in c8]))


######
b6=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[7]/div[1]/a/h4")
print(b6.text)
b6.click()
first_column.append(str(b6.text))
bos_bırak()

for c in range(1,4):
    c1 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[7]/div[2]/div/div/table/thead/tr/th["+str(c)+"]")))
    c2 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[7]/div[2]/div/div/table/tbody/tr[1]/td["+str(c)+"]")))
    c3 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[7]/div[2]/div/div/table/tbody/tr[2]/td["+str(c)+"]")))
    c4 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[7]/div[2]/div/div/table/tbody/tr[3]/td["+str(c)+"]")))
    c5 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[7]/div[2]/div/div/table/tbody/tr[4]/td["+str(c)+"]")))
    c6 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[7]/div[2]/div/div/table/tbody/tr[5]/td["+str(c)+"]")))
    c7 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[7]/div[2]/div/div/table/tbody/tr[6]/td["+str(c)+"]")))

    print([i.text for i in c1], [i.text for i in c2], [i.text for i in c3], [i.text for i in c4], [i.text for i in c5], [i.text for i in c6], [i.text for i in c7])
    first_column.append("")
    iki.append(str([i.text for i in c1]))
    uc.append(str([i.text for i in c2]))
    dort.append(str([i.text for i in c3]))
    bes.append(str([i.text for i in c4]))
    altı.append(str([i.text for i in c5]))
    yedi.append(str([i.text for i in c6]))
    sekiz.append(str([i.text for i in c7]))

######
b7=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[8]/div[1]/a/h4")
print(b7.text)
b7.click()
first_column.append(str(b7.text))
bos_bırak()

for c in range(1,4):
    c4,c5=[],[]
    c1 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[8]/div[2]/div/div/table/thead/tr/th["+str(c)+"]")))
    c2 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[8]/div[2]/div/div/table/tbody/tr[1]/td["+str(c)+"]")))
    try:
        c3 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[8]/div[2]/div/div/table/tbody/tr[2]/td["+str(c)+"]")))
    except:
        c3=[]
    try:
        c4 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[8]/div[2]/div/div/table/tbody/tr[3]/td["+str(c)+"]")))
    except:
        c4=[]
    try:
        c5 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[8]/div[2]/div/div/table/tbody/tr[4]/td["+str(c)+"]")))
    except:
        c5=[]
    print([i.text for i in c1], [i.text for i in c2], [i.text for i in c3], [i.text for i in c4], [i.text for i in c5])
    first_column.append("")
    iki.append(str([i.text for i in c1]))
    uc.append(str([i.text for i in c2]))
    dort.append(str([i.text for i in c3]))
    bes.append(str([i.text for i in c4]))
    altı.append(str([i.text for i in c5]))
######
b8=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[9]/div[1]/a/h4")
print(b8.text)
b8.click()
first_column.append(str(b8.text))
bos_bırak()

for c in range(1,4):
    c1 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[9]/div[2]/div/div/table/thead/tr/th["+str(c)+"]")))
    c2 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[9]/div[2]/div/div/table/tbody/tr[1]/td["+str(c)+"]")))
    c3 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[9]/div[2]/div/div/table/tbody/tr[2]/td["+str(c)+"]")))
    c4 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[9]/div[2]/div/div/table/tbody/tr[3]/td["+str(c)+"]")))
    c5 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[9]/div[2]/div/div/table/tbody/tr[4]/td["+str(c)+"]")))

    print([i.text for i in c1], [i.text for i in c2], [i.text for i in c3], [i.text for i in c4], [i.text for i in c5])
    first_column.append("")
    iki.append(str([i.text for i in c1]))
    uc.append(str([i.text for i in c2]))
    dort.append(str([i.text for i in c3]))
    bes.append(str([i.text for i in c4]))
    altı.append(str([i.text for i in c5]))
###

b9=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[10]/div[1]/a/h4")
print(b9.text)
b9.click()
first_column.append(str(b9.text))
bos_bırak()

b9_1 = wait.until(EC.presence_of_all_elements_located(
    (By.XPATH, "/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table[1]/thead/tr[1]/th")))
print([i.text for i in b9_1])
first_column.append("")
iki.append(str([i.text for i in b9_1]))
uc.append(" ")
dort.append(" ")
bes.append(" ")
altı.append(" ")
for c in range(1,4):
    c1 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table[1]/thead/tr[2]/th["+str(c)+"]")))
    c2 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table[1]/tbody/tr[1]/td["+str(c)+"]")))
    c3 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table[1]/tbody/tr[2]/td["+str(c)+"]")))
    c4 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table[1]/tbody/tr[3]/td["+str(c)+"]")))
    c5 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table[1]/tbody/tr[4]/td["+str(c)+"]")))

    print([i.text for i in c1], [i.text for i in c2], [i.text for i in c3], [i.text for i in c4], [i.text for i in c5])
    first_column.append("")
    iki.append(str([i.text for i in c1]))
    uc.append(str([i.text for i in c2]))
    dort.append(str([i.text for i in c3]))
    bes.append(str([i.text for i in c4]))
    altı.append(str([i.text for i in c5]))

b9_2 = wait.until(EC.presence_of_all_elements_located(
    (By.XPATH, "/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table[2]/thead/tr[1]/th")))
print([i.text for i in b9_2])
first_column.append("")
iki.append(str([i.text for i in b9_2]))
uc.append(" ")
dort.append(" ")
bes.append(" ")
altı.append(" ")


for c in range(1,4):
    c1 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table[2]/thead/tr[2]/th["+str(c)+"]")))
    c2 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[10]/div[2]/div/div/table[2]/tbody/tr/td["+str(c)+"]")))
    print([i.text for i in c1], [i.text for i in c2])
    first_column.append("")
    iki.append(str([i.text for i in c1]))
    uc.append(str([i.text for i in c2]))
    dort.append(" ")
    bes.append(" ")
#########
b10=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[11]/div[1]/a/h4")
print(b10.text)
b10.click()
first_column.append(str(b10.text))
bos_bırak()

for c in range(1,5):
    c1 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[11]/div[2]/div/div/table/thead/tr[2]/th["+str(c)+"]")))
    c2 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[11]/div[2]/div/div/table/tbody/tr[1]/td["+str(c)+"]")))

    print([i.text for i in c1], [i.text for i in c2] )
    first_column.append("")
    iki.append(str([i.text for i in c1]))
    uc.append(str([i.text for i in c2]))
    dort.append(" ")
    bes.append(" ")
#######
b11=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[12]/div[1]/a/h4")
print(b11.text)
b11.click()
first_column.append(str(b11.text))
bos_bırak()

for c in range(1,3):
    c1 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[12]/div[2]/div/div/table/thead/tr/th["+str(c)+"]")))
    c2 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[12]/div[2]/div/div/table/tbody/tr[1]/td["+str(c)+"]")))
    c3 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH, "/html/body/div[2]/div[1]/div[7]/div/div[12]/div[2]/div/div/table/tbody/tr[2]/td[" + str(c) + "]")))
    c4 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH, "/html/body/div[2]/div[1]/div[7]/div/div[12]/div[2]/div/div/table/tbody/tr[3]/td[" + str(c) + "]")))

    print([i.text for i in c1], [i.text for i in c2], [i.text for i in c3], [i.text for i in c4] )
    first_column.append("")
    iki.append(str([i.text for i in c1]))
    uc.append(str([i.text for i in c2]))
    dort.append(str([i.text for i in c3]))
    bes.append(str([i.text for i in c4]))
########
b12=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[13]/div[1]/a/h4")
print(b12.text)
b12.click()
first_column.append(str(b12.text))
bos_bırak()

for c in range(1,5):
    c1 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[13]/div[2]/div/div/table[1]/thead/tr/th["+str(c)+"]")))
    c2 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[7]/div/div[13]/div[2]/div/div/table[1]/tbody/tr[1]/td["+str(c)+"]")))
    c3 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH, "/html/body/div[2]/div[1]/div[7]/div/div[13]/div[2]/div/div/table[1]/tbody/tr[2]/td[" + str(c) + "]")))
    print([i.text for i in c1], [i.text for i in c2], [i.text for i in c3])
    first_column.append("")
    iki.append(str([i.text for i in c1]))
    uc.append(str([i.text for i in c2]))
    dort.append(str([i.text for i in c3]))
    bes.append(" ")
#########
#yukarı çık
yuk_cık=browser.find_element(By.XPATH,"/html/body/span/a").click()
sleep(10)
#########3
b13=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[1]/div[1]/a/h4")
print(b13.text)
b13.click()
first_column.append(str(b13.text))
bos_bırak()

for c in range(1,11):
    c1 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[1]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[1]")))
    c2 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[1]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[2]")))
    print([i.text for i in c1], [i.text for i in c2])
    first_column.append("")
    iki.append(str([i.text for i in c1]))
    uc.append(str([i.text for i in c2]))
    dort.append(" ")
    bes.append(" ")
######
b14=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[2]/div[1]/a/h4")
print(b14.text)
b14.click()
first_column.append(str(b14.text))
bos_bırak()

c1 = wait.until(EC.presence_of_all_elements_located(
    (By.XPATH, "/html/body/div[2]/div[1]/div[8]/div/div[2]/div[2]/div/div/table/thead/tr/th[1]")))
c2 = wait.until(EC.presence_of_all_elements_located(
    (By.XPATH, "/html/body/div[2]/div[1]/div[8]/div/div[2]/div[2]/div/div/table/thead/tr/th[2]")))
c3 = wait.until(EC.presence_of_all_elements_located(
    (By.XPATH, "/html/body/div[2]/div[1]/div[8]/div/div[2]/div[2]/div/div/table/thead/tr/th[3]")))

print([i.text for i in c1],[i.text for i in c2],[i.text for i in c3])
first_column.append("")
iki.append(str([i.text for i in c1]))
uc.append(str([i.text for i in c2]))
dort.append(str([i.text for i in c3]))
bes.append(" ")

for c in range(1,11):
    c1 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[2]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[1]")))
    c2 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[2]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[2]")))
    c3 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[2]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[3]")))

    print([i.text for i in c1], [i.text for i in c2],[i.text for i in c3])
    first_column.append("")
    iki.append(str([i.text for i in c1]))
    uc.append(str([i.text for i in c2]))
    dort.append(str([i.text for i in c3]))
    bes.append(" ")
######
b15=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[3]/div[1]/a/h4")
print(b15.text)
b15.click()
first_column.append(str(b15.text))
bos_bırak()

for c in range(1,4):
    c1 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[3]/div[2]/div/div/table/thead/tr/th["+str(c)+"]")))
    c2 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[3]/div[2]/div/div/table/tbody/tr[1]/td["+str(c)+"]")))
    c3 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[3]/div[2]/div/div/table/tbody/tr[2]/td["+str(c)+"]")))
    c4 = wait.until(EC.presence_of_all_elements_located(
        (By.XPATH, "/html/body/div[2]/div[1]/div[8]/div/div[3]/div[2]/div/div/table/tbody/tr[3]/td[" + str(c) + "]")))

    print([i.text for i in c1], [i.text for i in c2],[i.text for i in c3],[i.text for i in c4])
    first_column.append("")
    iki.append(str([i.text for i in c1]))
    uc.append(str([i.text for i in c2]))
    dort.append(str([i.text for i in c3]))
    bes.append(str([i.text for i in c4]))
#######
b16=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[4]/div[1]/a/h4")
print(b16.text)
b16.click()
first_column.append(str(b16.text))
bos_bırak()

b16_2 = wait.until(EC.presence_of_all_elements_located(
    (By.XPATH, "/html/body/div[2]/div[1]/div[8]/div/div[4]/div[2]/div/div/div[1]")))
print([i.text for i in b16_2])
first_column.append("")
iki.append(str([i.text for i in b16_2]))
uc.append(" ")
dort.append(" ")
bes.append(" ")

for c in range(1,4):
    c1 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[4]/div[2]/div/div/table/thead/tr/th["+str(c)+"]")))
    c2 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[4]/div[2]/div/div/table/tbody/tr[1]/td["+str(c)+"]")))
    c3 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[4]/div[2]/div/div/table/tbody/tr[2]/td["+str(c)+"]")))
    print([i.text for i in c1], [i.text for i in c2],[i.text for i in c3])
    first_column.append("")
    iki.append(str([i.text for i in c1]))
    uc.append(str([i.text for i in c2]))
    dort.append(str([i.text for i in c3]))
    bes.append(" ")

b16_3 = wait.until(EC.presence_of_all_elements_located(
    (By.XPATH, "/html/body/div[2]/div[1]/div[8]/div/div[4]/div[2]/div/div/div[2]/div[1]")))
print([i.text for i in b16_3])
first_column.append("")
iki.append(str([i.text for i in b16_3]))
uc.append(" ")
dort.append(" ")
bes.append(" ")

for c in range(1,4):
    c1 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[4]/div[2]/div/div/div[2]/table/thead/tr/th["+str(c)+"]")))
    c2 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[4]/div[2]/div/div/div[2]/table/tbody/tr[1]/td["+str(c)+"]")))
    c3 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[4]/div[2]/div/div/div[2]/table/tbody/tr[2]/td["+str(c)+"]")))
    print([i.text for i in c1], [i.text for i in c2],[i.text for i in c3])
    first_column.append("")
    iki.append(str([i.text for i in c1]))
    uc.append(str([i.text for i in c2]))
    dort.append(str([i.text for i in c3]))
    bes.append("")
######
b17=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[5]/div[1]/a/h4")
print(b17.text)
b17.click()
first_column.append(str(b17.text))
bos_bırak()

for c in range(1,4):
    c1 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[5]/div[2]/div/div/table[1]/tbody/tr["+str(c)+"]/td[1]")))
    c2 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[5]/div[2]/div/div/table[1]/tbody/tr["+str(c)+"]/td[2]")))
    print([i.text for i in c1], [i.text for i in c2])
    first_column.append("")
    iki.append(str([i.text for i in c1]))
    uc.append(str([i.text for i in c2]))
    dort.append(" ")

for c in range(4,7):
    c1 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[5]/div[2]/div/div/table[1]/tbody/tr["+str(c)+"]/td[1]")))
    c2 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[5]/div[2]/div/div/table[1]/tbody/tr["+str(c)+"]/td[2]")))
    c3 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[5]/div[2]/div/div/table[1]/tbody/tr["+str(c)+"]/td[3]")))
    print([i.text for i in c1], [i.text for i in c2],[i.text for i in c3])
    first_column.append("")
    iki.append(str([i.text for i in c1]))
    uc.append(str([i.text for i in c2]))
    dort.append(str([i.text for i in c3]))
print("\n")

c1 = wait.until(EC.presence_of_all_elements_located(
    (By.XPATH, "/html/body/div[2]/div[1]/div[8]/div/div[5]/div[2]/div/div/table[2]/thead/tr/th[1]")))
c2 = wait.until(EC.presence_of_all_elements_located(
    (By.XPATH, "/html/body/div[2]/div[1]/div[8]/div/div[5]/div[2]/div/div/table[2]/thead/tr/th[2]")))
first_column.append("")
iki.append(str([i.text for i in c1]))
uc.append(str([i.text for i in c2]))
dort.append(" ")



for c in range(1,11):
    c1 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[5]/div[2]/div/div/table[2]/tbody/tr["+str(c)+"]/td[1]")))
    c2 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[5]/div[2]/div/div/table[2]/tbody/tr["+str(c)+"]/td[2]")))
    print([i.text for i in c1], [i.text for i in c2])
    first_column.append("")
    iki.append(str([i.text for i in c1]))
    uc.append(str([i.text for i in c2]))
    dort.append(" ")
#########
b18=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[6]/div[1]/a/h4")
print(b18.text)
b18.click()
first_column.append(str(b18.text))
bos_bırak()

b18_2 = wait.until(EC.presence_of_all_elements_located(
    (By.XPATH, "/html/body/div[2]/div[1]/div[8]/div/div[6]/div[2]/div/div/table[1]/tbody/tr[1]/td[1]")))
b18_3 = wait.until(EC.presence_of_all_elements_located(
    (By.XPATH, "/html/body/div[2]/div[1]/div[8]/div/div[6]/div[2]/div/div/table[1]/tbody/tr[1]/td[2]")))
print([i.text for i in b18_2],[i.text for i in b18_3])
first_column.append("")
iki.append(str([i.text for i in b18_2]))
uc.append(str([i.text for i in b18_3]))
dort.append(" ")

for c in range(2,5):
    c1 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[6]/div[2]/div/div/table[1]/tbody/tr["+str(c)+"]/td[1]")))
    c2 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[6]/div[2]/div/div/table[1]/tbody/tr["+str(c)+"]/td[2]")))
    c3 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[6]/div[2]/div/div/table[1]/tbody/tr["+str(c)+"]/td[3]")))
    print([i.text for i in c1], [i.text for i in c2], [i.text for i in c3])
    first_column.append("")
    iki.append(str([i.text for i in c1]))
    uc.append(str([i.text for i in c2]))
    dort.append(str([i.text for i in c3]))

b18_4 = wait.until(EC.presence_of_all_elements_located(
    (By.XPATH, "/html/body/div[2]/div[1]/div[8]/div/div[6]/div[2]/div/div/table[1]/tbody/tr[5]/td[1]")))
b18_5 = wait.until(EC.presence_of_all_elements_located(
    (By.XPATH, "/html/body/div[2]/div[1]/div[8]/div/div[6]/div[2]/div/div/table[1]/tbody/tr[5]/td[2]")))
print([i.text for i in b18_4],[i.text for i in b18_5])
first_column.append("")
iki.append(str([i.text for i in b18_4]))
uc.append(str([i.text for i in b18_5]))

##########33
b19=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[7]/div[1]/a/h4")
print(b19.text)
b19.click()
first_column.append(str(b19.text))
bos_bırak()

c19_2 = wait.until(EC.presence_of_all_elements_located(
    (By.XPATH, "/html/body/div[2]/div[1]/div[8]/div/div[7]/div[2]/div/div/h4")))
print([i.text for i in c19_2])
first_column.append("")
iki.append(str([i.text for i in c19_2]))
uc.append(" ")
dort.append(" ")
bes.append(" ")
for c in range(1,6):
    c1 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[7]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[1]")))
    c2 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[7]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[2]")))
    print([i.text for i in c1], [i.text for i in c2])
    first_column.append("")
    iki.append(str([i.text for i in c1]))
    uc.append(str([i.text for i in c2]))
#########

b20=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[8]/div[1]/a/h4")
print(b20.text)
b20.click()
first_column.append(str(b20.text))
bos_bırak()

ac20_2 = wait.until(EC.presence_of_all_elements_located(
    (By.XPATH, "/html/body/div[2]/div[1]/div[8]/div/div[8]/div[2]/div/div/div[1]/h4")))
print([i.text for i in ac20_2])
first_column.append("")
iki.append(str([i.text for i in ac20_2]))
uc.append(" ")
dort.append(" ")
bes.append(" ")

for c in range(1,5):
    c1 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[8]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[1]")))
    c2 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[8]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[2]")))
    print([i.text for i in c1], [i.text for i in c2])
    first_column.append("")
    iki.append(str([i.text for i in c1]))
    uc.append(str([i.text for i in c2]))
###########



b21=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[9]/div[1]/a/h4")
print(b21.text)
b21.click()
first_column.append(str(b21.text))
bos_bırak()


c1 = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[9]/div[2]/div/div/table[1]/thead/tr[1]/th")))
print([i.text for i in c1])
first_column.append("")
iki.append(str([i.text for i in c1]))
uc.append(" ")

c1 = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[9]/div[2]/div/div/table[1]/thead/tr[2]/th[1]")))
c2 = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[9]/div[2]/div/div/table[1]/thead/tr[2]/th[2]")))
print([i.text for i in c1], [i.text for i in c2])
first_column.append("")
iki.append(str([i.text for i in c1]))
uc.append(str([i.text for i in c2]))


for c in range(1,130):
    try:
        c1 = wait1.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[9]/div[2]/div/div/table[1]/tbody/tr["+str(c)+"]/td[1]")))
    except:
        c1 = " "
    try:
        c2 = wait1.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[9]/div[2]/div/div/table[1]/tbody/tr["+str(c)+"]/td[2]")))
    except:
        c2= " "
    if c1!=" ":
        print([i.text for i in c1], [i.text for i in c2])
        first_column.append("")
        iki.append(str([i.text for i in c1]))
        uc.append(str([i.text for i in c2]))


c1 = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[9]/div[2]/div/div/table[2]/thead/tr[1]/th")))
print([i.text for i in c1])
first_column.append("")
iki.append(str([i.text for i in c1]))
uc.append(" ")

c1 = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[9]/div[2]/div/div/table[2]/thead/tr[2]/th[1]")))
c2 = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[9]/div[2]/div/div/table[2]/thead/tr[2]/th[2]")))
print([i.text for i in c1], [i.text for i in c2])
first_column.append("")
iki.append(str([i.text for i in c1]))
uc.append(str([i.text for i in c2]))

for c in range(1,78):
    try:
        c1 = wait1.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[9]/div[2]/div/div/table[2]/tbody/tr["+str(c)+"]/td[1]")))
    except:
        c1 = " "
    try:
        c2 = wait1.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[9]/div[2]/div/div/table[2]/tbody/tr["+str(c)+"]/td[2]")))
    except:
        c2= " "
    if c1!=" ":
        print([i.text for i in c1], [i.text for i in c2])
        first_column.append("")
        iki.append(str([i.text for i in c1]))
        uc.append(str([i.text for i in c2]))
##########


b22=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[10]/div[1]/a/h4")
print(b22.text)
b22.click()
first_column.append(str(b22.text))
bos_bırak()


c1 = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[10]/div[2]/div/div/table/thead/tr/th[1]")))
c2 = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[10]/div[2]/div/div/table/thead/tr/th[2]")))

print([i.text for i in c1], [i.text for i in c2])
first_column.append("")
iki.append(str([i.text for i in c1]))
uc.append(str([i.text for i in c2]))

for c in range(1,82):
    try:
        c1 = wait1.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[10]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[1]")))

    except:
        c1 = " "
    try:
        c2 = wait1.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[10]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[2]")))
    except:
        c2= " "
    if c1!=" ":
        print([i.text for i in c1], [i.text for i in c2])
        first_column.append("")
        iki.append(str([i.text for i in c1]))
        uc.append(str([i.text for i in c2]))

##############

b23=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[11]/div[1]/a/h4")
print(b23.text)
b23.click()
first_column.append(str(b23.text))
bos_bırak()

ac23_2 = wait.until(EC.presence_of_all_elements_located(
    (By.XPATH, "/html/body/div[2]/div[1]/div[8]/div/div[11]/div[2]/div/div/div[1]/h4")))
print([i.text for i in ac23_2])
first_column.append("")
iki.append(str([i.text for i in ac23_2]))
uc.append(" ")

ac23_3 = wait.until(EC.presence_of_all_elements_located(
    (By.XPATH, "/html/body/div[2]/div[1]/div[8]/div/div[11]/div[2]/div/div/table/thead/tr/th[1]")))
ac23_4 = wait.until(EC.presence_of_all_elements_located(
    (By.XPATH, "/html/body/div[2]/div[1]/div[8]/div/div[11]/div[2]/div/div/table/thead/tr/th[2]")))
print([i.text for i in ac23_3],[i.text for i in ac23_4])
first_column.append("")
iki.append(str([i.text for i in ac23_3]))
uc.append(str([i.text for i in ac23_4]))


for c in range(1,5):
    c1 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[11]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[1]")))
    c2 = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[11]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[2]")))
    print([i.text for i in c1], [i.text for i in c2])
    first_column.append("")
    iki.append(str([i.text for i in c1]))
    uc.append(str([i.text for i in c2]))

###########
b24=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[12]/div[1]/a/h4")
print(b24.text)
b24.click()
first_column.append(str(b24.text))
bos_bırak()

c1 = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[12]/div[2]/div/div/table/thead/tr/th[1]")))
c2 = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[12]/div[2]/div/div/table/thead/tr/th[2]")))

print([i.text for i in c1], [i.text for i in c2])
first_column.append("")
iki.append(str([i.text for i in c1]))
uc.append(str([i.text for i in c2]))

for c in range(1,82):
    try:
        c1 = wait1.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[12]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[1]")))

    except:
        c1 = " "
    try:
        c2 = wait1.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[12]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[2]")))
    except:
        c2= " "
    if c1!=" ":
        print([i.text for i in c1], [i.text for i in c2])
        first_column.append("")
        iki.append(str([i.text for i in c1]))
        uc.append(str([i.text for i in c2]))

##############
b25=browser.find_element(By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[13]/div[1]/a/h4")
print(b25.text)
b25.click()
first_column.append(str(b25.text))
bos_bırak()

c1 = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[13]/div[2]/div/div/table/thead/tr/th[1]")))
c2 = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[13]/div[2]/div/div/table/thead/tr/th[2]")))

print([i.text for i in c1], [i.text for i in c2])
first_column.append("")
iki.append(str([i.text for i in c1]))
uc.append(str([i.text for i in c2]))

for c in range(1,10):
    try:
        c1 = wait1.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[13]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[1]")))
    except:
        c1 = " "
    try:
        c2 = wait1.until(EC.presence_of_all_elements_located(
                    (By.XPATH,"/html/body/div[2]/div[1]/div[8]/div/div[13]/div[2]/div/div/table/tbody/tr["+str(c)+"]/td[2]")))
    except:
        c2= " "
    if c1!=" ":
        print([i.text for i in c1], [i.text for i in c2])
        first_column.append("")
        iki.append(str([i.text for i in c1]))
        uc.append(str([i.text for i in c2]))


####     *******dosyaya kaydetme
import xlsxwriter
workbook = xlsxwriter.Workbook('yök_atlas3.xlsx')
worksheet = workbook.add_worksheet()

for row_num, data in enumerate(first_column):
    worksheet.write(row_num, 0, data)
for row_num, data in enumerate(iki):
    worksheet.write(row_num, 1, data)
for row_num, data in enumerate(uc):
    worksheet.write(row_num, 2, data)
for row_num, data in enumerate(dort):
    worksheet.write(row_num, 3, data)
for row_num, data in enumerate(bes):
    worksheet.write(row_num, 4, data)
for row_num, data in enumerate(altı):
    worksheet.write(row_num, 5, data)
for row_num, data in enumerate(yedi):
    worksheet.write(row_num, 6, data)
for row_num, data in enumerate(sekiz):
    worksheet.write(row_num, 7, data)
for row_num, data in enumerate(dokuz):
    worksheet.write(row_num, 8, data)
workbook.close()
