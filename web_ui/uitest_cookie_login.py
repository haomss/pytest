from time import sleep
import yaml
from selenium import webdriver
from web_ui.base import Base


class TestCookieLogin(Base):

#1、需要退出当前所有谷歌浏览器
#2、执行以下复用浏览器启动命令
# mac上命令如下：
# /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
#
# 如果已经把谷歌浏览器的路径加入到环境变量中，可以使用
# Google\ Chrome --remote-debugging-port=9222

#需要退出当前所有谷歌浏览器

    def test_get_cookie(self):
        option = webdriver.ChromeOptions()
        option.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=option)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        sleep(3)
        cookie = self.driver.get_cookies()
        with open("uitestdata.yaml", encoding="UTF-8") as f:
            yaml.dump(cookie,f)

    def test_cookie_login(self): #可跳过扫码登录步骤
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        with open("uitestdata.yaml",encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)

                self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

                sleep(10)