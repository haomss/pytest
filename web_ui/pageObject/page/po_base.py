from time import sleep

import yaml
from selenium import webdriver
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Base():

    def __init__(self, base_driver=None):

        # 注解用，没有实际意义
        base_driver: WebDriver

        # 避免多次实例化driver
        if base_driver == None:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(5)
            self.driver.maximize_window()
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
            self.login()

        else:
            self.driver = base_driver

    # def teardown_class(self):
    #     self.driver.quit()

    def login(self):
        # self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        # sleep(10)
        # cookie = self.driver.get_cookies()
        # print(cookie)
        #
        # with open("potestdata.yaml", mode='w',encoding="UTF-8") as f:
        #     yaml.dump(cookie,f)

        with open("potestdata.yaml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)

                self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

    def wait_click(self, locator):

        return WebDriverWait(self.driver, 20).until(expected_conditions.presence_of_all_elements_located(locator))

    def find(self, by, value=None):

        if value == None:
            return self.driver.find_element(*by)

        else:
            return self.driver.find_element(by=by, value=value)

    def finds(self, by, value):
        # 如果传入的是元组，就解元组
        if value is None:
            return self.driver.find_elements(*by)
        # 如果传入两个参数则正常传参
        else:
            return self.driver.find_elements(by=by, value=value)

    def quit(self):

        self.driver.quit()
