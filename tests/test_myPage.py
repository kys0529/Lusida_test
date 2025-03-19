import pytest
from pages.myPage import MyPage

class TestMyPage:
    def test_open_order_list_page(self, driver):
        my_page = MyPage(driver)
        my_page.auto_login(driver)   
        my_page.open_order_list_page()
    
    @pytest.mark.skip(reason="미완성")
    def test_open_coupon_list_page(self, driver):
        pass
    
    @pytest.mark.skip(reason="미완성")
    def test_open_points_list_page(self, driver):
        pass
    
    @pytest.mark.skip(reason="미완성")
    def test_open_wishlist_page(self, driver):
        pass
    
    @pytest.mark.skip(reason="미완성")
    def test_open_my_posts_page(self, driver):
        pass