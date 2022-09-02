import yaml
import pytest

#获取数据的方法
def get_data():
    with open("./testdata.yml") as f:
        datas = yaml.safe_load(f)
        print(datas)
        return datas

class TestData:

    # @pytest.mark.parametrize(("a","b"),yaml.safe_load(open("./testdata.yml"))) #用yaml文件传参,参数为列表格式，如果传入字典格式，只能取出key
    # @pytest.mark.parametrize("a,b",[(1,2),(3,4)]) #str
    # @pytest.mark.parametrize(["a","b"], [(1, 2), (3, 5)]) #list 可修改
    # @pytest.mark.parametrize(("a", "b"), [(1, 2), (3, 6)])  # tuple 不可修改
    # @pytest.mark.parametrize(("a", "b"), [(1, 2), (3, 6)],ids = ["--1","--2"])  # ids 里是别名
    #参数的组合
    # @pytest.mark.parametrize("a", [1,2])
    # @pytest.mark.parametrize("b", [3,4])

    # @pytest.mark.parametrize("a,b,expected",yaml.safe_load(open("./testdata.yml"))["datas"],ids = yaml.safe_load(open("./testdata.yml"))["ids"])
    @pytest.mark.parametrize("a,b,expected",get_data()["datas"],ids = get_data()["ids"])
    def test_01(self,a,b,expected):

        assert a+b == expected



