import pytest

def setup_module():
    print("在该文件下所有case后执行一次")

def teardown_module():
    print("在该文件下所有case前执行一次")

def setup_function():
    print("不在类中的case前执行一次")

def teardown_function():
    print("不在类中的case后执行一次")


def test_04():
    print("--------4-------")
def test_05():
    print("--------5-------")

class TestClass():

    def setup_method(self):
        print("每个case前执行一次")

    def teardown_method(self):
        print("每个case后执行一次")

    def setup_class(self):
        print("该类下全部case前执行一次")

    def teardown_class(self):
        print("该类下全部case后执行一次")

    def test_01(self):
        print("--------1-------")
    def test_02(self):
        print("--------2-------")
    def test_03(self):
        print("--------3-------")