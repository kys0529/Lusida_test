import time
import pytest
from selenium import webdriver
from pages.purchasepage import PurchasePage
from pages.loginPage import LoginPage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys

def close_alert_if_present(driver):
        try:
            alert = Alert(driver)
            alert.accept()
            print("알림을 닫았습니다.")
        except:
            print("알림이 없습니다.")        

class TestPurchasePage:
    
    def test_purchase(self, driver: WebDriver):

        try:
            login_page = LoginPage(driver)
            login_page.open()

            time.sleep(2)

            wait = ws(driver, 10)
            wait.until(EC.url_contains("https://www.lusida.co.kr/shop/member.html?type=login"))
            assert "login" in driver.current_url

            login_page.input_password_and_email()

            login_btn = driver.find_element(By.CLASS_NAME, "login_btn")
            login_btn.click()

            #알림창이 나타나면 닫음
            close_alert_if_present(driver)

            wait = ws(driver, 10)
            wait.until(EC.url_contains("https://www.lusida.co.kr/index.html"))

            #로그인 후 메인 페이지로 이동 확인
            wait.until(EC.url_contains("https://www.lusida.co.kr/index.html"))

            time.sleep(10)
            
            purchase_page = PurchasePage(driver)

        except Exception as e:
            print(f"로그인 중 오류 발생: {e}")

        #     purchase_page = PurchasePage(driver)
            

        #     time.sleep()
        #     best50_menu = driver.find_element(By.CLASS_NAME, "hover_menu")
        #     actions = ActionChains(driver)
        #     actions.move_to_element(best50_menu).perform()

        #     time.sleep(2)
        #     best50_tab = driver.find_element(By.XPATH, "//a[contains(text(), 'BEST50')]")
        #     best50_tab.click()

        #     time.sleep(5)
        #     assert "shop/shopbrand.html?xcode=011" in driver.current_url, "BEST50의 페이지로 이동하지 않았습니다!"
            
        #     driver.save_screenshot("BEST50-이동-성공.jpg")

        # except NoSuchElementException as e:
        #     driver.save_screenshot('BEST50이동-실패-요소없음.jpg')
        #     assert False, f"페이지 로드 실패: 페이지를 찾을 수 없습니다."

        except TimeoutException as e:
            driver.save_screenshot('BEST50이동-실패-시간초과.jpg')
            assert False, f"페이지 로드 실패: 페이지 로드 시간이 초과했습니다."
        # except TimeoutException as e:
        #     driver.save_screenshot('BEST50이동-실패-시간초과.jpg')
        #     assert False, f"페이지 로드 실패: 페이지 로드 시간이 초과했습니다."
