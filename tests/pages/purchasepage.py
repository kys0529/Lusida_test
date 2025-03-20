from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

class PurchasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_best50(self):
        #BEST50 탭 클릭
        best50_tab = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "BEST50")))
        best50_tab.click()

    def select_random_product(self):
        #BEST50 페이지에서 랜덤으로 상품 클릭
        product_list = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a[href*='shopdetail.html']")))
        random_product = random.choice(product_list) #랜덤으로 상품 선택
        random_product.click()

    def select_color_and_size(self):
        #상품 상세 페이지에서 색상, 사이즈 랜덤 선택
        color_options = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".color-selector-class"))) # 색상 선택자
        size_options = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".size-selector-class"))) # 사이즈 선택자
        random.choice(color_options).click() #랜덤 색상 선택
        random.choice(size_options).click() #랜덤 사이즈 선택 

    def click_purchase_button(self):
        #구매 버튼 클릭
        purchase_button = self.driver.find_element(By.XPATH, "//button[contains(text(), '바로구매')]")
        purchase_button.click()