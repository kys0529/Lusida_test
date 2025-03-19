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
        main_page = MainPage(driver)
        auto_login = auto(driver)
        auto_login.auto_login(driver)

        # 로그인 페이지(accounts)로 이동했는지 확인
        wait = ws(driver, 10) #최대 10초까지 기다림
        wait.until(EC.url_contains("lusida.co.kr")) #URL 검증
        assert "lusida.co.kr" in driver.current_url #검증

        purchase_page = PurchasePage(driver)
        time.sleep(2)
        best50_tab = wait.until(EC.presence_of_element_located((By.XPATH, '//a[span[text()="BEST50"]]')))
        best50_tab.click()
        driver.back()

        NEW = wait.until(EC.presence_of_element_located((By.XPATH, '//a[span[text()="NEW"]]')))
        NEW.click()
        driver.back()

        time.sleep(2)

        #purchase_page.go_best50()

        #actions = ActionChains(driver)
        #actions.move_to_element(best50_menu).perform()

        #time.sleep(2)
        #best50_tab = driver.find_element(By.XPATH, "//a[contains(text(), 'BEST50')]")
        #best50_tab.click()

        #     time.sleep(5)
        #     assert "shop/shopbrand.html?xcode=011" in driver.current_url, "BEST50의 페이지로 이동하지 않았습니다!"
            
        #     driver.save_screenshot("BEST50-이동-성공.jpg")

        # except NoSuchElementException as e:
        #     driver.save_screenshot('BEST50이동-실패-요소없음.jpg')
        #     assert False, f"페이지 로드 실패: 페이지를 찾을 수 없습니다."
        # except TimeoutException as e:
        #     driver.save_screenshot('BEST50이동-실패-시간초과.jpg')
        #     assert False, f"페이지 로드 실패: 페이지 로드 시간이 초과했습니다."
