import selenium.webdriver as webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


user_agent ='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
driver_path = r"C:\\Users\\pc\\Desktop\\chromedriver.exe"
chrome_service = Service(driver_path)
chrome_options = Options()
chrome_options.add_argument(f'user-agent={user_agent}')
browser =webdriver.Chrome(service=chrome_service, options=chrome_options)
browser.get("https://sonuc.ysk.gov.tr/sorgu")
browser.maximize_window()
wait = WebDriverWait(browser, 30)
sleep(5)

yerleşim_yeri_ile_sorgula= wait.until(EC.element_to_be_clickable(
    (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-secim/div/div/div[2]/div/div/div[2]/button/div/div/div/div[2]/h4")))
sleep(3)
yerleşim_yeri_ile_sorgula.click()

sleep(3)
secim_adı = wait.until(EC.element_to_be_clickable(
    (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sorgu/div/div/div[2]/div[1]/div/div/form/div[1]/div/div/ng-select/div/div/div[2]/input")))
sleep(3)
secim_adı.click()
sleep(3)

mart_31_2019="/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sorgu/div/div/div[2]/div[1]/div/div/form/div[1]/div/div/ng-select/ng-dropdown-panel/div/div[2]/div[4]"
mart_30_2014="/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sorgu/div/div/div[2]/div[1]/div/div/form/div[1]/div[1]/div/ng-select/ng-dropdown-panel/div/div[2]/div[10]"

secimi_sec=wait.until(EC.element_to_be_clickable((By.XPATH,mart_30_2014)))
sleep(3)
secimi_sec.click()
sleep(3)

secim_adı_secme_click=wait.until(EC.element_to_be_clickable(
    (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sorgu/div/div/div[2]/div[1]/div/div/form/div[1]/div[2]/div/ng-select/div/div/div[2]/input")))
sleep(3)
secim_adı_secme_click.click()
sleep(3)

k=1
# belediye başkanlığını indirmek için k=1
# belediye meclis üyeliğini indirmek için k=2
# büyükşehir belediye başkanlığı için k=3
# il genel meclis üyeliği seçimleri için k=4 olmalı
secim_adı_secme=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sorgu/div/div/div[2]/div[1]/div/div/form/div[1]/div[2]/div/ng-select/ng-dropdown-panel/div/div[2]/div["+str(k)+"]")))
sleep(3)
secim_adı_secme.click()
sleep(3)

devam_et =wait.until(EC.element_to_be_clickable(
    (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sorgu/div/div/div[2]/div[1]/div/div/form/div[2]/div/div/button[1]")))
sleep(3)
devam_et.click()

il_num=1

ili_sec_click= wait.until(EC.element_to_be_clickable(
    (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/fieldset/form/div[1]/div[2]/div[1]/ng-select/div/div/div[2]/input")))
sleep(5)
ili_sec_click.click()

ili_sec = wait.until(EC.element_to_be_clickable(
    (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/fieldset/form/div[1]/div[2]/div[1]/ng-select/ng-dropdown-panel/div/div[2]/div["+str(il_num)+"]")))
sleep(5)
ili_sec.click()
sleep(5)

ilce_num=1
n=1

while n<4:
    if il_num==82 and ilce_num==1 and k==1:
        break
    if il_num==82 and ilce_num==1 and k==2:
        break
    if il_num==31 and ilce_num==1 and k==3:
        break
    if il_num==52 and ilce_num==1 and k==4:
        break
    try:
        try:
            try:
                ilce_sec_click = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/fieldset/form/div[1]/div[2]/div[2]/ng-select/div/div/div[3]/input")))
                sleep(5)
                ilce_sec_click.click()
                sleep(5)
            except:
                ilce_sec_click = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/fieldset/form/div[1]/div[2]/div[2]/ng-select/div/div/div[2]/input")))
                sleep(5)
                ilce_sec_click.click()
                sleep(5)
            ilce_sec = wait.until(EC.element_to_be_clickable(
                (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/fieldset/form/div[1]/div[2]/div[2]/ng-select/ng-dropdown-panel/div/div[2]/div["+str(ilce_num)+"]")))
            sleep(5)
            ilce_sec.click()
            sleep(5)

            sorgula_btn = wait.until(EC.element_to_be_clickable(
                (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/fieldset/form/div[2]/div/div/button")))
            sleep(5)
            sorgula_btn.click()
            sleep(5)

            browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            indir = wait.until(EC.element_to_be_clickable(
                (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-yurtici-muhtarlik-listesi/fieldset/div[2]/div/button")))
            sleep(3)
            indir.click()

            kabul_et = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/ngb-modal-window/div/div/div[2]/div/button[1]")))
            sleep(3)
            kabul_et.click()
            sleep(3)

            ilce_num+=1
        except:
            browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            try:
                ilce_sec_click = wait.until(EC.element_to_be_clickable(
                    (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/fieldset/form/div[1]/div[2]/div[2]/ng-select/div/div/div[3]/input")))
                sleep(5)
                ilce_sec_click.click()
                sleep(5)

            except:

                ilce_sec_click = wait.until(EC.element_to_be_clickable(
                    (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/fieldset/form/div[1]/div[2]/div[2]/ng-select/div/div/div[2]/input")))
                sleep(5)
                ilce_sec_click.click()
                sleep(5)

            ilce_sec = wait.until(EC.element_to_be_clickable(
                (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/fieldset/form/div[1]/div[2]/div[2]/ng-select/ng-dropdown-panel/div/div[2]/div[" + str(ilce_num) + "]")))
            sleep(5)
            ilce_sec.click()
            sleep(5)

            sorgula_btn = wait.until(EC.element_to_be_clickable(
                (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/fieldset/form/div[2]/div/div/button")))
            sleep(5)
            sorgula_btn.click()
            sleep(5)

            browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            indir = wait.until(EC.element_to_be_clickable(
                (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-yurtici-muhtarlik-listesi/fieldset/div[2]/div/button")))
            sleep(3)
            indir.click()

            kabul_et = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/ngb-modal-window/div/div/div[2]/div/button[1]")))
            sleep(3)
            kabul_et.click()
            sleep(3)

            browser.execute_script("window.scrollTo(document.body.scrollHeight,0)")
            ilce_num += 1

    except:
        try:
            il_num+=1
            ilce_num=1

            ilce_sec = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/fieldset/form/div[1]/div[2]/div[2]/ng-select/ng-dropdown-panel/div/div[2]/div[1]")))
            sleep(5)
            ilce_sec.click()
            sleep(5)

            ili_sec_click = wait.until(EC.element_to_be_clickable(
                (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/fieldset/form/div[1]/div[2]/div[1]/ng-select/div/div/div[3]/input")))
            sleep(5)
            ili_sec_click.click()

            ili_sec = wait.until(EC.element_to_be_clickable(
                (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/fieldset/form/div[1]/div[2]/div[1]/ng-select/ng-dropdown-panel/div/div[2]/div[" + str(il_num) + "]")))
            sleep(5)
            ili_sec.click()
            sleep(5)
        except:
            ilce_num = 1

            ilce_sec = wait.until(EC.element_to_be_clickable(
                (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/fieldset/form/div[1]/div[2]/div[2]/ng-select/ng-dropdown-panel/div/div[2]/div[1]")))
            sleep(5)
            ilce_sec.click()
            sleep(5)

            ili_sec_click = wait.until(EC.element_to_be_clickable(
                (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/fieldset/form/div[1]/div[2]/div[1]/ng-select/div/div/div[3]/input")))
            sleep(5)
            ili_sec_click.click()

            ili_sec = wait.until(EC.element_to_be_clickable(
                (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/fieldset/form/div[1]/div[2]/div[1]/ng-select/ng-dropdown-panel/div/div[2]/div[" + str(il_num) + "]")))
            sleep(5)
            ili_sec.click()
            sleep(5)

