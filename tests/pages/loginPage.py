
from xml.dom.minidom import Element
from conftest import driver
from selenium.webdriver.common.by import By  # By 모듈 추가
#from config import EMAIL, PASSWORD

class LoginPage: 
  
  URL = "https://www.lusida.co.kr/shop/member.html?type=login"

  def __init__(self,driver):
    self.driver = driver

  def open(self):
    self.driver.get(self.URL)

  def input_password_and_email(self):
    input_email = self.driver.find_element(By.XPATH, "//input[@type='text']")
    input_email.send_keys("lusidatest")
    input_password = self.driver.find_element(By.XPATH, "//input[@type='password']")
    input_password.send_keys("123123123^^")
    
  def click_login_button(self):
    login = self.driver.find_element(By.XPATH, "//button[contains(text(), '로그인')]")
    login.click()
