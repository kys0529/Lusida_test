from ast import parse
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
from urllib.parse import quote

class TestSearchPage:    
    #상품 검색
    def test_search_items(self, driver: WebDriver):
        try:
            ITEMS_XPATH = "//img"
            SCROLL_XPATH = "//div/ul[@class='item-order']"
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

            # 스크롤
            scroll_element = driver.find_element(By.XPATH, SCROLL_XPATH)
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'nearest'});", scroll_element)
            time.sleep(2)

            driver.save_screenshot("메인페이지-검색-성공.png")
        except NoSuchElementException as e:
            driver.save_screenshot("메인페이지-검색-실패-노서치.png")
            assert False
        except TimeoutException as e:
            driver.save_screenshot("메인페이지-검색-실패-타임에러.png")
            assert False

    # 상품 필터링
    def test_item_filter(self, driver: WebDriver):
        try:
            ITEMS_XPATH = "//img"
            SCROLL_XPATH = "//div/ul[@class='item-order']"
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

            # 필터 버튼들의 XPATH
            filters_xpath = {
                "인기순": "//ul[@class='item-order']//span[contains(text(), '인기순')]",
                "신상품": "//ul[@class='item-order']//span[contains(text(), '신상품')]",
                "높은가격": "//ul[@class='item-order']//span[contains(text(), '높은가격')]",
                "낮은가격": "//ul[@class='item-order']//span[contains(text(), '낮은가격')]"
            }

            # 필터 순서대로 클릭하여 결과 확인
            for filter_name, filter_xpath in filters_xpath.items():            
                wait.until(EC.element_to_be_clickable((By.XPATH, filter_xpath)))

                # 필터 클릭
                driver.find_element(By.XPATH, filter_xpath).click()

                # 스크롤
                scroll_element = driver.find_element(By.XPATH, SCROLL_XPATH)
                driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'nearest'});", scroll_element)
                
                time.sleep(3)

                # 필터 클릭 후 결과 로딩 대기
                wait = ws(driver, 10)

                 # 스크린샷 저장
                driver.save_screenshot(f"필터-적용-{filter_name}.png")

                # 필터 적용 후 아이템 확인
                items = driver.find_elements(By.XPATH, ITEMS_XPATH)
                assert len(items) > 0

        except NoSuchElementException as e:
            driver.save_screenshot("검색-실패-노서치.png")
            assert False
        except TimeoutException as e:
            driver.save_screenshot("메인페이지-검색-실패-타임에러.png")
            assert False