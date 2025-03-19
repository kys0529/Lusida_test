import pytest
from pages.QA import QA

class TestQA:
    @pytest.mark.skip(reason="확인 테스트")
    def test_QA(self, driver):
        try:
            Qa = QA(driver)
            Qa.QA_assert(driver)
        except Exception as e:
            print(f"[오류] 예상치 못한 에러 발생: {e}")
            assert False, "테스트 실패 - 알 수 없는 예외 발생"
