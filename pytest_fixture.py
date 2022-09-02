import pytest


class Test_demo():
    def test01(self,myfixture):
        print("----01-------")
        myf = myfixture
        print(myf)

    def test02(self,myfixture_1):
        print("----02-------")



if __name__ == "__main__":
    Test_demo()