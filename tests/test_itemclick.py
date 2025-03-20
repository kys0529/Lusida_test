import pytest
import random
import time
from pages.mainPage import MainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import Select
from pages.autologin import auto


class TestCLICK:
    
    def test_item_click(self, driver: WebDriver):
        try:
            auto_login = auto(driver)
            auto_login.auto_login(driver)

            #main_page = MainPage(driver)
            #main_page.open()

            wait = ws(driver, 10)  # 최대 10초 대기

            best50_tab = wait.until(EC.presence_of_element_located((By.XPATH, '//a[span[text()="BEST50"]]')))
            best50_tab.click()

            wait.until(EC.presence_of_element_located((By.XPATH, '//img[@alt="상품 섬네일"]')))

            item_list = wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//img[@alt="상품 섬네일"]')))
            random_num = random.randint(0, 6)
            item_list[random_num].click()

            time.sleep(2)

            color_select = driver.find_element(By.XPATH, '//select[@label="색상"]')
            color_options = Select(color_select)
            
            options = color_options.options
            if len(options) > 1:  # 옵션이 1개 이상 있을 경우
                random_color_index = random.randint(1, len(options) - 1)  # 0은 '옵션 선택'이므로 제외
                color_options.select_by_index(random_color_index)  # 랜덤 색상 선택

            size_select = driver.find_element(By.XPATH, '//select[@label="사이즈"]')
            size_options = Select(size_select)
            size_opts = size_options.options
            if len(size_opts) > 1:  # 옵션이 1개 이상 있을 경우
                random_size_index = random.randint(1, len(size_opts) - 1)  # 0은 '옵션 선택'이므로 제외
                size_options.select_by_index(random_size_index)  # 랜덤 사이즈 선택
            
            button = wait.until(EC.presence_of_element_located((By.XPATH, '//a[text()="바로구매"]')))
            button.click()
            
            time.sleep(5)

        
        except Exception as e:
            print(f"[오류] 예상치 못한 에러 발생: {e}")
            assert False, "테스트 실패 - 알 수 없는 예외 발생"

