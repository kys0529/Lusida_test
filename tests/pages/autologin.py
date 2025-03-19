import time
from pages.mainPage import MainPage
from pages.loginPage import LoginPage
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class auto:
    def __init__(self, driver):
        self.driver = driver

    def auto_login(self, driver):
        try:
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
            
        except Exception as e:
            print(f"[오류] 예상치 못한 에러 발생: {e}")
            assert False, "테스트 실패 - 알 수 없는 예외 발생"
