import time
import pytest
from pages.purchasepage import PurchasePage
from pages.mainPage import MainPage
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from pages.autologin import auto

def close_alert_if_present(driver):
        try:
            alert = Alert(driver)
            alert.accept()
            print("알림을 닫았습니다.")
        except:
            print("알림이 없습니다.")        

class TestPurchasePage:

    def test_purchase(self, driver: WebDriver):
        auto_login = auto(driver)
        auto_login.auto_login(driver)
        
        wait = ws(driver, 10) #최대 10초까지 기다림

        purchase_page = PurchasePage(driver)
        time.sleep(2)
        best50_tab = wait.until(EC.presence_of_element_located((By.XPATH, '//a[span[text()="BEST50"]]')))
        best50_tab.click()
        driver.back()

        NEW = wait.until(EC.presence_of_element_located((By.XPATH, '//a[span[text()="NEW"]]')))
        NEW.click()
        driver.back()

        time.sleep(2)
