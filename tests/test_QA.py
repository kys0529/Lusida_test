import pytest
from pages.QA import QA

class TestQA:
    
    @pytest.mark.parametrize("inquiry", ["FAQ", "상품문의", "배송문의"])
    def test_QA(self, driver,inquiry):
        try:
            Qa = QA(driver)
            Qa.QA_assert(driver,inquiry)
            Qa.QA_search("입금",inquiry)
            
        except Exception as e:
            print(f"[오류] 예상치 못한 에러 발생: {e}")
            assert False, "테스트 실패 - 알 수 없는 예외 발생"
