import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from pages.mainPage import MainPage
from selenium.common.exceptions import NoSuchElementException , TimeoutException

class QA:
    def __init__(self, driver):
        self.driver =driver
        self.action = ActionChains(self.driver)

    def QA_assert(self,driver:WebDriver):
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
        