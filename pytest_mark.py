import pytest

class TestClass():

    @pytest.mark.demo  #标记
    @pytest.mark.smoke  #标记
    def test_01(self):
        print("--------1-------")

    @pytest.mark.demo  #标记
    def test_02(self):
        print("--------2-------")




# pytest pytest_mark.py -m 'smoke and demo' -vs #运行标记是smoke和demo的；'smoke or demo'同
# pytest pytest_mark.py -m smoke -vs   #只运行标记为smoke的