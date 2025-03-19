from ast import parse
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
from urllib.parse import quote

class TestSearchPage:    
    #상품 검색
    def test_search_items(self, driver: WebDriver):
        try:
            ITEMS_XPATH = "//img"
            mainPage = MainPage(driver)
            mainPage.open()

            wait = ws(driver, 10)
            wait.until(EC.url_contains("lusida.co.kr"))
            assert "lusida.co.kr" in driver.current_url

            # 검색어 입력
            mainPage.search_text_input('가디건')

            ws(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, ITEMS_XPATH))
            )
            
            items = driver.find_elements(By.XPATH, ITEMS_XPATH)

            assert len(items) > 0

            driver.save_screenshot("메인페이지-검색-성공.png")
        except NoSuchElementException as e:
            driver.save_screenshot("메인페이지-검색-실패-노서치.png")
            assert False
        except TimeoutException as e:
            driver.save_screenshot("메인페이지-검색-실패-타임에러.png")
            assert False