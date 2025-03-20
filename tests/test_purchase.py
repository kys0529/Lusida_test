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
from selenium.common.exceptions import NoSuchElementException , TimeoutException, ElementClickInterceptedException

def close_alert_if_present(driver):
        try:
            alert = Alert(driver)
            alert.accept()
            print("알림을 닫았습니다.")
        except:
            print("알림이 없습니다.")        

class TestPurchasePage:
    
    def test_purchase(self, driver: WebDriver):

        #try:
        main_page = MainPage(driver)
        auto_login = auto(driver)
        auto_login.auto_login(driver)

        # 로그인 페이지(accounts)로 이동했는지 확인
        wait = ws(driver, 10) #최대 10초까지 기다림
        wait.until(EC.url_contains("lusida.co.kr")) #URL 검증
        assert "lusida.co.kr" in driver.current_url #검증

        purchase_page = PurchasePage(driver)
        time.sleep(2)

        #알림창이 나타나면 닫음
        close_alert_if_present(driver)

        best50_tab = wait.until(EC.presence_of_element_located((By.XPATH, '//a[span[text()="BEST50"]]')))
        best50_tab.click()
        driver.save_screenshot("BEST50-이동-성공.jpg")
        time.sleep(3)

        MAX_RETRIES = 5
        retry_count = 0

        while retry_count < MAX_RETRIES:
            try:
                  
                #랜덤 상품 선택
                purchase_page.select_random_product()

                time.sleep(1)
                print("상품 선택 성공!")
                break
        
            except ElementClickInterceptedException as e:
                  print("상품을 찾을 수 없음, 재시도 중...({retry_count + 1}/{MAX_RETRIES})")
                  retry_count += 1
                  time.sleep(1)
        
            except TimeoutException as e:
                print(f"상품 선택 Timeout, 재시도 중... ({retry_count + 1}/{MAX_RETRIES})")
                retry_count += 1
                time.sleep(1)

        if retry_count == MAX_RETRIES:
              pytest.fail("상품 선택 실패: 최대 재시도 횟수 초과")

        #색상과 사이즈 선택
        purchase_page.select_color_and_size()

        time.sleep(2)

        #구매버튼 클릭
        purchase_page.click_purchase_button()

        time.sleep(5)
        driver.save_screenshot("BEST50-상품상세옵션-구매-성공.jpg")