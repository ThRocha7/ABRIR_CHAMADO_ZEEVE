from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import pandas as pd
import time
import resources

service = Service()
options = webdriver.ChromeOptions()
chrome_prefs = {
            "profile.default_content_settings.popups": 0,
            "download.prompt_for_download": True,
            "plugins.always_open_pdf_externally": True
        }
options.add_experimental_option("prefs", chrome_prefs)
options.add_experimental_option("detach", True)
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=service, options=options)


driver.get(resources.url)

def click_xpath(element):
    try:
        xpath = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, element))
        )
        xpath.click()
    except:
        driver.quit()

def write_xpath(element, text):
    try:
        text = str(text)
        xpath = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, element))
        )
        xpath.send_keys(text)
    except:
        driver.quit()

def write_enter_xpath(element, text):
    try:
        text = str(text)
        xpath = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, element))
        )
        xpath.send_keys(text)
        time.sleep(1)
        xpath.send_keys(Keys.ENTER)
    except:
        driver.quit()


a = input('... ')

while a != 'ok':
    a = input('... ')

inicar_apps = '//*[@id="aSideMenuNewRequest"]'
click_xpath(inicar_apps)

pesquisar_chamado = '//*[@id="txtSearch"]'
write_enter_xpath(pesquisar_chamado, 'Realizar Pagamento | Oracle')

chamado = '//*[@id="containerRequests"]/div[1]/div/div'
chamado_certo = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, chamado))).text

if 'Realizar Pagamento | Oracle' in chamado_certo:
    btn_solicitar = '//*[@id="btnRequest-31221fa2-e652-48f3-887d-1d1384b2ca20"]'
    click_xpath(btn_solicitar)
