import pytest

class TestClass:
    def test_01(self):
        assert 3 == 3

    def test_02(self):
        assert 5 == 6

if __name__ == "__main__":
    pytest.main(["-s","D:\untitled20211210_01\package1\package1_01\dist\\test_pytest001.py"])


