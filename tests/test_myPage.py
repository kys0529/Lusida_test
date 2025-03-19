from pages.myPage import MyPage

class TestMyPage:
    def test_open_order_list_page(self, driver):
        my_page = MyPage(driver)
        my_page.auto_login(driver)
        
    def test_open_order_list_page(self, driver):
        pass
    
    def test_open_coupon_list_page(self, driver):
        pass
    
    def test_open_points_list_page(self, driver):
        pass
    
    def test_open_wishlist_page(self, driver):
        pass
    
    def test_open_my_posts_page(self, driver):
        pass