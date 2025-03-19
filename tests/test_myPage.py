import pytest
from pages.myPage import MyPage

class TestMyPage:
    @pytest.mark.skip(reason="테스트 완료!")
    @pytest.mark.parametrize("text", ["주문내역", "쿠폰내역", "적립금내역", "위시리스트", "내가쓴글"])
    def test_open_mypage_hide_menu(self, driver, text):
        try:
            my_page = MyPage(driver)
            my_page.auto_login(driver)   
            my_page.open_mypage_hide_menu(text)
        except Exception as e:
            print(f"[❗] {e}")
    
    @pytest.mark.skip(reason="미완성")      
    def test_open_shop_detail_page(self, driver):
        try:
            my_page = MyPage(driver)
            my_page.auto_login(driver)
            my_page.open_shop_detail_page()
        except Exception as e:
            print(f"[❗] {e}")