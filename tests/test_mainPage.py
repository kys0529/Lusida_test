import time
import pytest
from pages.qa import QA
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

    @pytest.mark.skip(reason=" 고객센터 확인 테스트")
    def test_QA(self,driver):
        Qa = QA(driver)
        Qa.QA_assert(driver)