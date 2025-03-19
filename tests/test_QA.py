import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from pages.mainPage import MainPage
from pages.loginPage import LoginPage
from selenium.common.exceptions import NoSuchElementException , TimeoutException

class QA:
    #@pytest.mark.skip(reason="확인 테스트")
    def test_QA(self,driver:WebDriver):
        QA()