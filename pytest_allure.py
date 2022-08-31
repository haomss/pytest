import allure
import pytest

@allure.severity(allure.severity_level.CRITICAL) #设置执行等级
@allure.feature("登录模块") #父模块
class TestLogin():

    @allure.severity(allure.severity_level.NORMAL)#设置执行等级
    @allure.title("这条case叫：登录成功") #设置case的名称
    @allure.story("登录成功") #子模块
    @allure.testcase("http://www.baidu.com") #添加一个链接
    def test_login_success_1(self):
        with allure.step("步骤一：打开应用"):
            print("打开应用")
        with allure.step("步骤二：登录"):
            print("登录")
        with allure.step("步骤三：输入用户名密码"):
            print("输入用户名密码")
        print("登录成功---1")

    @allure.story("登录成功")
    def test_login_success_2(self):
        print("登录成功---2")

    @allure.story("登录失败")
    def test_login_failure_3(self):
        print("登录失败---3")

    @allure.story("登录失败")
    def test_login_failure_4(self):
        print("登录失败---用户名缺失")

    @allure.story("登录失败")
    def test_login_failure_5(self):
        print("登录失败---密码缺失")

@allure.feature("搜索模块")
class TestSearch():

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("case1")
    def test_case1(self):
        print("case1")

    @allure.story("case1")
    def test_case2(self):
        print("case2")

# pytest pytest_allure.py --allure-features='登录模块' -vs    #执行父模块为"登录模块"的case
# pytest pytest_allure.py --allure-stories='登录成功' -vs    #执行子模块为"登录成功"的case
# pytest pytest_allure.py --allure-features='登录模块' --allure-stories='登录成功' -vs     #同时使用时，先执行features

# pytest pytest_allure.py  --alluredir ./result1   #生成报告中间文件
# allure serve ./result1   #生成测试报告，默认打开浏览器

#  allure generate ./result1 --clean  #生成报告在当前目录 用浏览器打开
#  allure generate ./result1 -o 目录  #指定报告生成的目录
#  pytest pytest_allure.py --allure-severities='normal' -vs  #按等级执行

#allure open -h 127.0.0.1 -p 8883 ./allure-report/  #指定ip端口 打开报告

class Test_xxx():

    def test_attach_text(self):
        allure.attach("这是一个纯文本", name="文本",attachment_type=allure.attachment_type.TEXT)

    def test_allure_html(self):
        allure.attach(''''<body>这是一个html块<body>''',name="html块",attachment_type=allure.attachment_type.HTML)

    def test_allure_photo(self):
        allure.attach.file("/",name="图片",attachment_type=allure.attachment_type.JPG)

    def test_allure_video(self):
        allure.attach.file("/",name="视频",attachment_type=allure.attachment_type.MP4)

