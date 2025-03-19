import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from pages.mainPage import MainPage
from pages.loginPage import LoginPage
from selenium.common.exceptions import NoSuchElementException , TimeoutException

class TestMainPage:
    def setup(self):
        self.driver = webdriver.Chrome()
    
    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip(reason="아직 테스트 케이스 발동 안함")
    def test_open_main_page(self, driver: WebDriver):
    
        try:
            main_page = MainPage(driver)
            main_page.open()

        # 로그인 페이지(accounts)로 이동했는지 확인
            wait = ws(driver, 10) #최대 10초까지 기다림
            wait.until(EC.url_contains("lusida.co.kr")) #URL 검증
            assert "lusida.co.kr" in driver.current_url #검증

        except NoSuchElementException as e:
            assert False

    #@pytest.mark.skip(reason="확인 테스트")
    def test_QA(self,driver:WebDriver):
        try:
            main_page = MainPage(driver)
            main_page.open()

            wait = ws(driver, 10) #최대 10초까지 기다림
            wait.until(EC.url_contains("lusida.co.kr")) #URL 검증
            assert "lusida.co.kr" in driver.current_url #검증

            main_page.click_by_LINK_TEXT_DROP_DOWN("고객센터")
            time.sleep(2)
            main_page.click_by_LINK_TEXT_DROP_DOWN("FAQ")
            
            #검증 로직
            #main_page.assert_is_displayed(faq_link,"FAQ")

            wait.until(EC.url_contains("https://www.lusida.co.kr/board")) #URL 검증
            assert "https://www.lusida.co.kr/board" in driver.current_url #검증
            driver.back()
            
            main_page.click_by_LINK_TEXT_DROP_DOWN("고객센터")
            time.sleep(2)
            main_page.click_by_LINK_TEXT_DROP_DOWN("상품문의")

            wait.until(EC.url_contains("https://www.lusida.co.kr/board")) #URL 검증
            assert "https://www.lusida.co.kr/board" in driver.current_url #검증
            driver.back()

            main_page.click_by_LINK_TEXT_DROP_DOWN("고객센터")
            time.sleep(2)
            main_page.click_by_LINK_TEXT_DROP_DOWN("배송문의")

            wait.until(EC.url_contains("https://www.lusida.co.kr/board")) #URL 검증
            assert "https://www.lusida.co.kr/board" in driver.current_url #검증
            driver.back()

            time.sleep(2)
        
        except NoSuchElementException as e:
            assert False


    #자동로그인
    @pytest.mark.skip(reason="아직 테스트 케이스 발동 안함")
    def test_login_test(self,driver:WebDriver):
        try:
            main_page = MainPage(driver)
            login_page = LoginPage(driver)
            main_page.open()
        
            wait = ws(driver, 10) #최대 10초까지 기다림
            wait.until(EC.url_contains("lusida.co.kr")) #URL 검증
            assert "lusida.co.kr" in driver.current_url #검증

            time.sleep(2)

            login_link = wait.until(EC.presence_of_element_located((By.XPATH, '//a[@href="/shop/member.html?type=login"]')))
            login_link.click()
            time.sleep(2)
            
            login_page.input_password_and_email()

            time.sleep(2)
            login_btn = driver.find_element(By.CLASS_NAME, "login_btn")
            login_btn.click()

            time.sleep(2)
            alert = wait.until(EC.alert_is_present())
            alert.accept()  # 확인 버튼 클릭

            time.sleep(7)
            wait.until(EC.url_contains("lusida.co.kr")) #URL 검증
            assert "lusida.co.kr" in driver.current_url , "로그인 후 메인 페이지로 돌아오지 않았습니다."
            
            driver.save_screenshot("로그인 성공.jpg")

        except NoSuchElementException as e:
            driver.save_screenshot('로그인-실패-요소없음.jpg')  # 요소를 찾을 수 없을 때
            assert False, f"로그인 실패: 필수 요소를 찾을 수 없습니다. {e}"

        except TimeoutException as e:
            driver.save_screenshot('로그인-실패-시간초과.jpg')  # 시간 초과 발생
            assert False, f"로그인 실패: 페이지 로드가 시간이 초과되었습니다. {e}"

        except AssertionError as e:
            driver.save_screenshot('로그인-실패-검증오류.jpg')  # 검증 오류 발생
            assert False, f"로그인 실패: {e}"

        except Exception as e:
            driver.save_screenshot('로그인-실패-기타오류.jpg')  # 기타 예외 상황
            assert False, f"로그인 실패: 알 수 없는 오류 발생 - {e}"
