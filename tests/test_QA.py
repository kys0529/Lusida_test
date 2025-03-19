import pytest
from pages.qa import QA

class TESTQA:
    #@pytest.mark.skip(reason="확인 테스트")
    def test_QA(self,driver):
        Qa = QA(driver)
        Qa.QA_assert(driver)
        