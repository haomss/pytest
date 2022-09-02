import pytest

# pip install pytest-rerunfailures  #重试
@pytest.mark.flaky(reruns=3,reruns_delay=1) #eruns=3重试3次，reruns_delay=1隔1秒
class Test_rerun():

    # @pytest.mark.flaky(reruns=3,reruns_delay=1) #eruns=3重试3次，reruns_delay=1隔1秒
    def test_01(self):
        print("#####-1-#####")
        assert 1==2

    def test_02(self):
        print("#####-2-#####")

# pip install pytest-assume  #断言失败后继续执行后面的断言
class Test_assume():

    def test_03(self):
        print("%%%%%-3-%%%%%")
        # assert 1==2 #断言失败后，后面的不会执行
        pytest.assume(1 == 2) #断言失败后，后面的代码继续执行
        print("-----------------")
        pytest.assume(1 == 3)
        print("-----------------")
        pytest.assume(1 == 4)
        print("-----------------")


# pip install pytest-xdist  #并发;case间相互独立时使用节省运行时间
class Test_xdist():

    def test_04(self): #执行：pytest  -n 3；3条并发
        print("@@@@@-4-@@@@@")


# pip install pytest-ordering #更改用例执行顺序；
class Test_ordering():

    @pytest.mark.run(order=-1)
    def test_05(self):
        print("*****-5-*****")

    def test_06(self):
        print("*****-6-*****")
    @pytest.mark.run(order = 1)
    def test_07(self):
        print("*****-7-*****")