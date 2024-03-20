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
wait = WebDriverWait(browser, 60)
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

cb_ikinci_tür=wait.until(EC.element_to_be_clickable(
    (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sorgu/div/div/div[2]/div[1]/div/div/form/div[1]/div[1]/div/ng-select/ng-dropdown-panel/div/div[2]/div[11]/div")))
sleep(3)
cb_ikinci_tür.click()
sleep(3)

devam_et =wait.until(EC.element_to_be_clickable(
    (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sorgu/div/div/div[2]/div[1]/div/div/form/div[2]/div/div/button[1]")))
sleep(3)
devam_et.click()

sleep(3)
detay_yurt_ici= wait.until(EC.element_to_be_clickable(
    (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-tum-dunya/fieldset/div[1]/table/tbody/tr[2]/td[1]/button")))
sleep(5)
detay_yurt_ici.click()
sleep(5)

n=15
i=2
il_num=2
ilce_atla=3
il_atla=3

while i<20:
    if i<=11:
        if il_atla>=4:
            browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            try:
                sleep(4)
                browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                atla = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-yurtici-il-listesi/fieldset/div[1]/ngb-pagination/ul/li["+str(il_atla)+"]")))
                sleep(10)
                atla.click()
            except:

                browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                geri_dön = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[2]/button")))
                sleep(3)
                geri_dön.click()

                devam_et = wait.until(EC.element_to_be_clickable(
                    (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sorgu/div/div/div[2]/div[1]/div/div/form/div[2]/div/div/button[1]")))
                sleep(3)
                devam_et.click()

                sleep(4)
                browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                atla = wait.until(EC.element_to_be_clickable(
                    (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-yurtici-il-listesi/fieldset/div[1]/ngb-pagination/ul/li["+str(il_atla)+"]")))
                sleep(60)
                atla.click()
        try:
            il_adı = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-yurtici-il-listesi/fieldset/div[1]/table/tbody/tr["+str(il_num)+"]/td[2]")))
            sleep(7)
            il_ad = [i.text for i in il_adı]

            if il_adı==['MARDİN'] and ilce_atla==4 and i==2:
                il_num+=1
                i==2
                ilce_atla==3
            if il_adı==['ERZURUM'] and ilce_atla==5 and i==2:
                il_num+=1
                i==2
                ilce_atla==3
            if il_adı==['BALIKESİR'] and ilce_atla==5 and i==2:
                il_num+=1
                i==2
                ilce_atla==3
            if il_adı==['İZMİR'] and ilce_atla==6 and i==2:
                il_num+=1
                i==2
                ilce_atla==3

            ili_sec = wait.until(EC.element_to_be_clickable(
                (By.XPATH,
                 "/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-yurtici-il-listesi/fieldset/div[1]/table/tbody/tr["+str(il_num)+"]/td[1]/button")))
            sleep(7)
            ili_sec.click()

        except:
            geri_dön = wait.until(EC.element_to_be_clickable(
                (By.XPATH,
                 "/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[2]/button")))
            sleep(3)
            geri_dön.click()

            devam_et = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sorgu/div/div/div[2]/div[1]/div/div/form/div[2]/div/div/button[1]")))
            sleep(3)
            devam_et.click()

            browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

            atla = wait.until(EC.element_to_be_clickable(
                (By.XPATH,
                 "/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-yurtici-il-listesi/fieldset/div[1]/ngb-pagination/ul/li["+str(il_atla)+"]")))
            sleep(60)
            atla.click()

            il_adı = wait.until(EC.presence_of_all_elements_located(
                (By.XPATH,
                 "/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-yurtici-il-listesi/fieldset/div[1]/table/tbody/tr["+str(il_num)+"]/td[2]")))
            sleep(7)
            il_ad = [i.text for i in il_adı]

            if il_adı==['MARDİN'] and ilce_atla==4 and i==2:
                ili_sec=+1
                i==2
            if il_adı==['ERZURUM'] and ilce_atla==5 and i==2:
                ili_sec=+1
                i==2
            if il_adı==['BALIKESİR'] and ilce_atla==5 and i==2:
                ili_sec=+1
                i==2
            if il_adı==['İZMİR'] and ilce_atla==6 and i==2:
                ili_sec=+1
                i==2


            ili_sec = wait.until(EC.element_to_be_clickable(
                (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-yurtici-il-listesi/fieldset/div[1]/table/tbody/tr["+str(il_num)+"]/td[1]/button")))
            sleep(7)
            ili_sec.click()


        try:
            try:
                if ilce_atla>=4:
                    sonraki_sayfa=wait.until(EC.element_to_be_clickable(
                        (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-yurtici-ilce-listesi/fieldset/div[1]/ngb-pagination/ul/li["+str(ilce_atla)+"]")))
                    sleep(3)
                    sonraki_sayfa.click()

                ilce_sec= wait.until(EC.element_to_be_clickable(
                    (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-yurtici-ilce-listesi/fieldset/div[1]/table/tbody/tr["+str(i)+"]/td[1]/button")))
                sleep(5)
                ilce_sec.click()

                indir= wait.until(EC.element_to_be_clickable(
                    (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-yurtici-muhtarlik-listesi/fieldset/div[2]/div/button")))
                sleep(3)
                indir.click()

                kabul_et= wait.until(EC.element_to_be_clickable(
                    (By.XPATH,"/html/body/ngb-modal-window/div/div/div[2]/div/button[1]")))
                sleep(3)
                kabul_et.click()
                sleep(3)

                browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

                geri_dön=wait.until(EC.element_to_be_clickable(
                    (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[2]/button")))
                sleep(3)
                geri_dön.click()

                devam_et = wait.until(EC.element_to_be_clickable(
                    (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sorgu/div/div/div[2]/div[1]/div/div/form/div[2]/div/div/button[1]")))
                sleep(3)
                devam_et.click()
                i+=1
            except:
                geri_dön = wait.until(EC.element_to_be_clickable(
                    (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[2]/button")))
                sleep(3)
                geri_dön.click()

                devam_et = wait.until(EC.element_to_be_clickable(
                    (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sorgu/div/div/div[2]/div[1]/div/div/form/div[2]/div/div/button[1]")))
                sleep(3)
                devam_et.click()

                if ilce_atla >= 4:
                    sonraki_sayfa = wait.until(EC.element_to_be_clickable(
                        (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-yurtici-ilce-listesi/fieldset/div[1]/ngb-pagination/ul/li["+str(ilce_atla)+"]")))
                    sleep(3)
                    sonraki_sayfa.click()

                ilce_sec = wait.until(EC.element_to_be_clickable(
                    (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-yurtici-ilce-listesi/fieldset/div[1]/table/tbody/tr["+str(i)+"]/td[1]/button")))
                sleep(5)
                ilce_sec.click()

                indir = wait.until(EC.element_to_be_clickable(
                    (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-yurtici-muhtarlik-listesi/fieldset/div[2]/div/button")))
                sleep(3)
                indir.click()

                kabul_et = wait.until(EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/ngb-modal-window/div/div/div[2]/div/button[1]")))
                sleep(3)
                kabul_et.click()
                sleep(3)
                browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

                geri_dön = wait.until(EC.element_to_be_clickable(
                    (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[2]/button")))
                sleep(3)
                geri_dön.click()

                devam_et = wait.until(EC.element_to_be_clickable(
                    (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sorgu/div/div/div[2]/div[1]/div/div/form/div[2]/div/div/button[1]")))
                sleep(3)
                devam_et.click()
                i += 1

        except:
            i=2
            il_num+=1
            ilce_atla=3

            sleep(5)
            geri_dön2 = wait.until(EC.element_to_be_clickable(
                (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[2]/button")))
            sleep(3)
            geri_dön2.click()

            devam_et2 = wait.until(EC.element_to_be_clickable(
                (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sorgu/div/div/div[2]/div[1]/div/div/form/div[2]/div/div/button[1]")))
            sleep(10)
            devam_et2.click()
            sleep(3)
    else:
        i=2
        ilce_atla+=1
    if il_num==12:
        i=2
        il_num=2
        il_atla+=1
    if il_atla==11 and il_num==3:
        break


geri_dön=wait.until(EC.element_to_be_clickable(
    (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[2]/button")))
sleep(3)
geri_dön.click()


yurt_dısı_sec = wait.until(EC.element_to_be_clickable(
    (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sorgu/div/div/div[2]/div[1]/div/div/form/div[1]/div[2]/div/div[3]/label")))
sleep(5)
yurt_dısı_sec.click()

devam_et =wait.until(EC.element_to_be_clickable(
    (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sorgu/div/div/div[2]/div[1]/div/div/form/div[2]/div/div/button[1]")))
sleep(3)
devam_et.click()

n=15
i=2
il_num=2
ilce_atla=3
il_atla=3
secim_cevresi_atla=3
while i<20:
    if i<=11:
        if i == 7 and il_num == 8 and secim_cevresi_atla == 3:
            break
        try:
            secim_cevresi = wait.until(EC.element_to_be_clickable(
                (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-yurtdisi-tum/fieldset/div[1]/table/tbody/tr["+str(secim_cevresi_atla)+"]/td[1]/button")))
            sleep(5)
            secim_cevresi.click()
        except:
            geri_dön = wait.until(EC.element_to_be_clickable(
                (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[2]/button")))
            sleep(10)
            geri_dön.click()

            devam_et = wait.until(EC.element_to_be_clickable(
                (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sorgu/div/div/div[2]/div[1]/div/div/form/div[2]/div/div/button[1]")))
            sleep(10)
            devam_et.click()
            secim_cevresi = wait.until(EC.element_to_be_clickable(
                (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-yurtdisi-tum/fieldset/div[1]/table/tbody/tr["+str(secim_cevresi_atla)+"]/td[1]/button")))
            sleep(5)
            secim_cevresi.click()

        if il_atla>=4:
            browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            try:
                if secim_cevresi_atla==2:
                    atla = wait.until(EC.element_to_be_clickable(
                        (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-yurtdisi-ulke-listesi/fieldset/div[1]/ngb-pagination/ul/li["+str(il_atla)+"]/a")))
                    sleep(10)
                if secim_cevresi_atla == 3:
                    atla = wait.until(EC.element_to_be_clickable(
                        (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-yurtdisi-gumruk-listesi/fieldset/div[1]/ngb-pagination/ul/li[" + str(il_atla) + "]/a")))
                    sleep(3)
                atla.click()
            except:
                geri_dön = wait.until(EC.element_to_be_clickable(
                    (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[2]/button")))
                sleep(3)
                geri_dön.click()

                devam_et = wait.until(EC.element_to_be_clickable(
                    (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sorgu/div/div/div[2]/div[1]/div/div/form/div[2]/div/div/button[1]")))
                sleep(3)
                devam_et.click()

                secim_cevresi = wait.until(EC.element_to_be_clickable(
                    (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-yurtdisi-tum/fieldset/div[1]/table/tbody/tr[" + str(secim_cevresi_atla) + "]/td[1]/button")))
                sleep(5)
                secim_cevresi.click()

                browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                sleep(3)
                if secim_cevresi_atla == 2:
                    atla = wait.until(EC.element_to_be_clickable(
                        (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-yurtdisi-ulke-listesi/fieldset/div[1]/ngb-pagination/ul/li[" + str(il_atla) + "]/a")))
                    sleep(10)
                if secim_cevresi_atla == 3:
                    atla = wait.until(EC.element_to_be_clickable(
                        (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-yurtdisi-gumruk-listesi/fieldset/div[1]/ngb-pagination/ul/li[" + str(il_atla) + "]/a")))
                    sleep(3)
                atla.click()
        try:
            try:
                if secim_cevresi_atla == 2:
                    ili_sec =wait.until(EC.element_to_be_clickable(
                        (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-yurtdisi-ulke-listesi/fieldset/div[1]/table/tbody/tr["+str(il_num)+"]/td[1]/button")))
                    sleep(7)
                    ili_sec.click()
                if ilce_atla!=3:
                    try:
                        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                        sleep(3)
                        if secim_cevresi_atla==2:
                            sonraki_sayfa=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-yurtdisi-dis-temsilcilik-listesi/fieldset/div[1]/ngb-pagination/ul/li["+str(ilce_atla)+"]/a")))
                            sleep(3)
                        elif secim_cevresi_atla==3:
                            sonraki_sayfa = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-yurtdisi-gumruk-listesi/fieldset/div[1]/ngb-pagination/ul/li[" + str(ilce_atla) + "]/a")))
                            sleep(3)
                        sonraki_sayfa.click()
                    except:
                        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                        geri_dön = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[2]/button")))
                        sleep(3)
                        geri_dön.click()

                        devam_et = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sorgu/div/div/div[2]/div[1]/div/div/form/div[2]/div/div/button[1]")))
                        sleep(3)
                        devam_et.click()

                        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                        sleep(3)
                        if secim_cevresi_atla == 2:
                            sonraki_sayfa = wait.until(EC.element_to_be_clickable(
                                (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-yurtdisi-dis-temsilcilik-listesi/fieldset/div[1]/ngb-pagination/ul/li[" + str(ilce_atla) + "]/a")))
                            sleep(3)
                        if secim_cevresi_atla == 3:
                            sonraki_sayfa = wait.until(EC.element_to_be_clickable(
                                (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-yurtdisi-gumruk-listesi/fieldset/div[1]/ngb-pagination/ul/li[" + str(ilce_atla) + "]/a")))
                            sleep(3)
                        sonraki_sayfa.click()
                sleep(4)
                if secim_cevresi_atla == 2:
                    ilce_sec= wait.until(EC.element_to_be_clickable(
                        (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-yurtdisi-dis-temsilcilik-listesi/fieldset/div[1]/table/tbody/tr["+str(i)+"]/td[1]/button")))
                    sleep(6)
                    ilce_sec.click()

                    indir = wait.until(EC.element_to_be_clickable(
                        (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-yurtdisi-dis-temsilcilik-sandik-listesi/fieldset/div[2]/div/button")))
                    sleep(10)
                    indir.click()

                if secim_cevresi_atla == 3:
                    ilce_secl = wait.until(EC.element_to_be_clickable(
                        (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-yurtdisi-gumruk-listesi/fieldset/div[1]/table/tbody/tr["+str(i)+"]/td[1]/button")))
                    sleep(6)
                    ilce_secl.click()
                    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

                    indir = wait.until(EC.element_to_be_clickable(
                        (By.XPATH,"html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-yurtdisi-gumruk-sandik-listesi/fieldset/div[2]/div/button")))
                    sleep(10)
                    indir.click()
                    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")


                kabul_et= wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/ngb-modal-window/div/div/div[2]/div/button[1]")))
                sleep(10)
                kabul_et.click()
                sleep(3)

                geri_dön=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[2]/button")))
                sleep(10)
                geri_dön.click()

                devam_et = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sorgu/div/div/div[2]/div[1]/div/div/form/div[2]/div/div/button[1]")))
                sleep(10)
                devam_et.click()
                i+=1

            except:
                geri_dön = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[2]/button")))
                sleep(10)
                geri_dön.click()

                devam_et = wait.until(EC.element_to_be_clickable(
                    (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sorgu/div/div/div[2]/div[1]/div/div/form/div[2]/div/div/button[1]")))
                sleep(10)
                devam_et.click()

                secim_cevresi = wait.until(EC.element_to_be_clickable(
                    (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-yurtdisi-tum/fieldset/div[1]/table/tbody/tr["+str(secim_cevresi_atla)+"]/td[1]/button")))
                sleep(5)
                secim_cevresi.click()

                browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
                sleep(3)
                sonraki_sayfa = wait.until(EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-yurtdisi-dis-temsilcilik-listesi/fieldset/div[1]/ngb-pagination/ul/li["+str(ilce_atla)+"]/a")))
                sleep(3)
                sonraki_sayfa.click()

                sleep(4)
                if secim_cevresi_atla == 2:
                    ilce_sec = wait.until(EC.element_to_be_clickable(
                        (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-yurtdisi-dis-temsilcilik-listesi/fieldset/div[1]/table/tbody/tr[" + str(i) + "]/td[1]/button")))
                    sleep(6)
                    ilce_sec.click()

                browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")

                indir = wait.until(EC.element_to_be_clickable(
                    (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[1]/div/div/app-yurtdisi-dis-temsilcilik-sandik-listesi/fieldset/div[2]/div/button")))
                sleep(10)
                indir.click()

                kabul_et = wait.until(EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/ngb-modal-window/div/div/div[2]/div/button[1]")))
                sleep(10)
                kabul_et.click()
                sleep(3)

                geri_dön = wait.until(EC.element_to_be_clickable(
                    (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[2]/button")))
                sleep(10)
                geri_dön.click()

                devam_et = wait.until(EC.element_to_be_clickable(
                    (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sorgu/div/div/div[2]/div[1]/div/div/form/div[2]/div/div/button[1]")))
                sleep(10)
                devam_et.click()
                i += 1
        except:
            i=2
            il_num+=1
            ilce_atla=3
            geri_dön2 = wait.until(EC.element_to_be_clickable(
                (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sonuc/div/div/div[2]/div[2]/button")))
            sleep(3)
            geri_dön2.click()

            devam_et2 = wait.until(EC.element_to_be_clickable(
                (By.XPATH,"/html/body/app-root/app-vatandas/div[2]/app-vatandas-asistan-arsiv-sorgu/div/div/div[2]/div[1]/div/div/form/div[2]/div/div/button[1]")))
            sleep(10)
            devam_et2.click()
            sleep(3)
    elif i==7 and il_num==8 and secim_cevresi_atla==3:
        break
    else:
        i=2
        ilce_atla+=1

    if il_num==12:
        i=2
        il_num=2
        il_atla+=1

    if il_atla==10 and il_num==5:
        secim_cevresi_atla+=1



