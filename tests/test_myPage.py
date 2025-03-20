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
    
    #@pytest.mark.skip(reason="미완성")   
    @pytest.mark.parametrize("url", [
        "https://www.lusida.co.kr/shop/shopdetail.html?branduid=53337&search=&xcode=054&mcode=002&scode=&special=1&GfDT=bm90W15A",
    ])   
    def test_add_product_in_wishlist(self, driver, url):
        try:
            my_page = MyPage(driver)
            my_page.auto_login(driver)
            my_page.add_product_in_wishlist(url)
        except Exception as e:
            print(f"[❗] {e}")