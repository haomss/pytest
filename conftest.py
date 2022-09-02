import pytest

# fixture作用范围@pytest.fixture(scope="")：
#     function：默认作用域，每一个函数或方法都会调用
#     class：每个测试类只执行一次
#     module：每个.py文件只调用一次
#     package：每个python包只执行一次
#     session：整个会话只执行一次，即运行项目时，整个过程只执行一次。


# @pytest.fixture()
@pytest.fixture(params=["---参数1---","---参数2---"])#参数化
def myfixture(request):
    print("-----myfixture---%s--"% request.param)

    # return request.param

    yield request.param #类似return
    print("这里类似---teardown--") #作用域是同fixture的作用范围（scope=""）

@pytest.fixture()
def myfixture_1():
    print("-----myfixture_1-----")
