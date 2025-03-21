from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as ws
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys #key입력 임포트
from selenium.webdriver.common.action_chains import ActionChains

class MainPage:
    URL = "https://www.lusida.co.kr/"
    SEARCH_INPUT_ID = "headerSearchKeyword"

    #객체 -> 인스턴스화 \ 제가 원하는 설정으로 셋업 하는 함수
    def __init__(self,driver: WebDriver):
        self.driver = driver
        self.search = "search"
    
    def open(self):
        self.driver.get(self.URL)
    
    def search_text_input(self, item_name: str, pause_between_chars=1):
        """item_name 을 자모 단위(또는 영문자)로 순차 입력하며 타이핑"""
        search_input_box = self.driver.find_element(By.NAME, self.search)
        
        # 1) ActionChains 객체 생성
        actions = ActionChains(self.driver)
        
        # 2) 검색창을 클릭하여 포커스 이동
        #    (이미 포커스가 가 있다면 생략 가능)
        actions.move_to_element(search_input_box).click().pause(0.1)
        
        # 3) item_name의 각 글자를 순차 입력 + 글자마다 잠시 pause
        for char in item_name:
            actions.send_keys(char).pause(pause_between_chars)

        actions.send_keys(Keys.ENTER)
        
        # 4) 한 번에 실행
        actions.perform()
    
    #click 드롭박스 함수 마우스를 드롭다운 한 곳에 가져가서 누르기
    def click_by_LINK_TEXT_DROP_DOWN(self, link_text: str):
        click_button = ws(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, link_text)))
        actions = ActionChains(self.driver)
        actions.move_to_element(click_button).click().perform()

    #click 링크텍스트 함수 
    def click_by_LINK_TEXT(self, link_text: str):
        click_button = ws(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, link_text)))
        click_button.click()
    
    def search_text_enter(self):
        search_input_box = self.driver.find_element(By.ID, self.SEARCH_INPUT_ID)
        actions = ActionChains(self.driver)
        actions.move_to_element(search_input_box).click().pause(0.1)
        actions.send_keys(Keys.ENTER)
        actions.perform()

    def assert_is_displayed(element, name):
        is_displayed = element.is_displayed()
        if not is_displayed: 
            assert is_displayed, f"{name} 항목 표시X."
        
    
