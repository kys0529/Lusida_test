
from xml.dom.minidom import Element
from conftest import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
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
