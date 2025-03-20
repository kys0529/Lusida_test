import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class ITEMCLICK:
    def __init__(self, driver):
        self.driver = driver
        self.action = ActionChains(self.driver)

    def open_shop_detail_page(self,driver):

        item_list = ws(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//img[@alt="상품 섬네일"]')))
        item_list.click()
        # random_num = random.randint(0, len(item_list) - 1)
        # item_uid = item_list[random_num].find_element(By.XPATH, ".//p[@class='abcd']/span").get_attribute("data-uid")
        # item_href = item_list[random_num].find_element(By.XPATH, ".//a").get_attribute("href")
        
        # print(f"random_num : {random_num}")
        # print(f"item_uid : {item_uid}")
        # print(f"item_href : {item_href}")