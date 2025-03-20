from ast import parse
import random
import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from pages.mainPage import MainPage
from pages.autologin import auto
from selenium.common.exceptions import NoSuchElementException , TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

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

    # 상품 구매
    def test_item_purchase(self, driver: WebDriver):
        try:
            auto_login = auto(driver)
            auto_login.auto_login(driver)
        except Exception as e:
            pytest.skip(f"로그인 실패로 테스트 스킵: {e}")

        try:
            CLICK_XPATH = "//div//dt//a//img[@alt='상품 섬네일']"
            mainPage = MainPage(driver)

            # 검색어 입력
            mainPage.search_text_input('가디건')

            ws(driver, 30).until(
                EC.presence_of_element_located((By.XPATH, CLICK_XPATH))
            )

            # 특정 요소까지 부드럽게 스크롤
            def scroll_to_element(driver, element):
                driver.execute_script("arguments[0].scrollIntoView({ behavior: 'smooth', block: 'center' });", element)

            # 랜덤으로 아이템 선택하고 클릭하는 함수
            def scroll_and_click(driver, xpath):
                # 아이템 리스트 가져오기
                items = driver.find_elements(By.XPATH, xpath)
                if items:
                    # 랜덤으로 선택할 아이템
                    selected_item = random.choice(items)
                    
                    # 선택한 요소까지 스크롤
                    scroll_to_element(driver, selected_item)

                    # 스크롤 후 대기 (2~3초)
                    time.sleep(random.uniform(2, 3))

                    # 부드럽게 마우스 이동 후 클릭
                    actions = ActionChains(driver)
                    actions.move_to_element(selected_item).click().perform()

                    # 클릭 후 대기 (1~2초)
                    time.sleep(random.uniform(1, 2))  

                    # 스크린샷 저장
                    driver.save_screenshot("선택-성공.png")

            # 페이지를 아래로 내리면서 랜덤 클릭
            items = driver.find_elements(By.XPATH, CLICK_XPATH)
            if items:
                scroll_and_click(driver, CLICK_XPATH)

        except TimeoutException as e:
            driver.save_screenshot("메인페이지-검색-실패-타임에러.png")
            assert False