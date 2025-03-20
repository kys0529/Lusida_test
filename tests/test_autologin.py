import pytest
from pages.autologin import auto

class TestautoLogin:
    def test_auto_login(self, driver):
        try:
            auto_login = auto(driver)
            auto_login.auto_login(driver)

        except Exception as e:
            print(f"[오류] 예상치 못한 에러 발생: {e}")
            assert False, "테스트 실패 - 알 수 없는 예외 발생"
