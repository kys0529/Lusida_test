import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC

from pages.mainPage import MainPage
from pages.loginPage import LoginPage

class MyPage:
    def __init__(self, driver):
        self.driver = driver
        
    def auto_login(self, driver):
        main_page = MainPage(driver)
        login_page = LoginPage(driver)
        
        main_page.open()
        wait = ws(driver, 10) 
        wait.until(EC.url_contains("lusida.co.kr")) 
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
        alert.accept()
        time.sleep(2)
        
        wait.until(EC.url_contains("lusida.co.kr")) 
        time.sleep(2)
    
    def open_order_list_page(self):
        pass
    
    def open_coupon_list_page(self):
        pass
    
    def open_points_list_page(self):
        pass
    
    def open_wishlist_page(self):
        pass
    
    def open_my_posts_page(self):
        pass