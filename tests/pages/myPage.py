import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

from pages.mainPage import MainPage
from pages.loginPage import LoginPage

class MyPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = ws(self.driver, 10)
        self.action = ActionChains(self.driver)
        
    def auto_login(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        
        main_page.open()
        self.wait.until(EC.url_contains("lusida.co.kr")) 
        time.sleep(2)

        login_link = self.wait.until(EC.presence_of_element_located((By.XPATH, '//a[@href="/shop/member.html?type=login"]')))
        login_link.click()
        time.sleep(2)
        
        login_page.input_password_and_email()
        time.sleep(2)
        
        login_btn = driver.find_element(By.CLASS_NAME, "login_btn")
        login_btn.click()
        time.sleep(2)
        
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()
        time.sleep(2)
        
        self.wait.until(EC.url_contains("lusida.co.kr")) 
        time.sleep(2)
    
    def open_mypage_hide_menu(self, text):
        mypage_btn = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "마이페이지")))
        self.action.move_to_element(mypage_btn).perform()
        time.sleep(2)
        
        hide_menu_btn = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, text)))
        hide_menu_btn.click()
        time.sleep(2)
        
    def add_product_in_wishlist(self, url):
        self.driver.get(url)
        self.wait.until(EC.url_contains(url))
        time.sleep(2)
        
        if self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "opt-wrap"))) is not None:
            option_lists = self.wait.until(EC.presence_of_all_elements_located((By.NAME, "optionlist[]")))
            
            for option in option_lists:
                dropdown = Select(option)
                dropdown.select_by_index(1)
                time.sleep(2)
        else:
            print("옵션 선택 사항 X")
        
        wish_btn = self.wait.until(EC.presence_of_element_located((By.ID, "wishBtn")))
        wish_btn.click()
        time.sleep(2)
        
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()
        time.sleep(2)
        
        # TODO: 요소를 찾지 못함 -> 해결하기
        # item_list = ws(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, "//dl[@class='item-list']")))
        # random_num = random.randint(0, len(item_list) - 1)
        # item_uid = ws(item_list[1], 10).until(EC.presence_of_element_located((By.XPATH, ".//p[@class='abcd']/span"))).get_attribute("data-uid")
        # item_href = ws(item_list[1], 10).until(EC.presence_of_element_located((By.XPATH, ".//a"))).get_attribute("href")
        
        # print(f"random_num : {random_num}")
        # print(f"item_uid : {item_uid}")
        # print(f"item_href : {item_href}")