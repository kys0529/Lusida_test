from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
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
     # 색상 선택 (드롭다운)
        color_dropdown = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[name='optionlist[]'][label='색상'], select[name='optionlist[]'][label='color']")))
        color_select = Select(color_dropdown)
        color_options = [opt for opt in color_select.options if opt.get_attribute("value") !=""]  # 첫 번째 빈 옵션 제외

        selected_color = color_select.first_selected_option.get_attribute("value")
        color_options = [opt for opt in color_options if opt.get_attribute("value") != selected_color]

        # 1+1 상품인지 확인: 색상 옵션이 2개인 경우 1+1 상품으로 처리
        if len(color_options) == 2:
            color_options[0].click()  # 첫 번째 색상 선택
            color_options[1].click()  # 두 번째 색상 선택
            print("색상 2개 선택 (1+1 상품)")
        elif len(color_options) > 0:
            # 일반 상품: 색상 선택
            random.choice(color_options).click()
            print("색상 선택 완료")
        else:
            raise ValueError("색상 옵션이 없습니다.") 

        try:
            size_dropdown = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "select[name='optionlist[]'][label='사이즈'], select[name='optionlist[]'][label='size']")))
            size_select = Select(size_dropdown)

            size_options = [opt for opt in size_select.options if opt.get_attribute("value") != ""]  # 첫 번째 빈 옵션 제외
            selected_size = size_select.first_selected_option.get_attribute("value")
            size_options = [opt for opt in size_options if opt.get_attribute("value") != selected_size]

            #사이즈를 랜덤으로 선택
            random.choice(size_options).click()
            print("사이즈 선택 완료")
        except:
            print("사이즈 선택 없음 (1+1 상품)") #사이즈가 없는 경우 예외 처리

    def click_purchase_button(self):
        #구매 버튼 클릭
        purchase_button = self.driver.find_element(By.XPATH, "//a[contains(text(), '바로구매')]")
        purchase_button.click()