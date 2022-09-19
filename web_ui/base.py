#!/usr/bin/env python
# -*- conding: utf-8 -*-

import os

from selenium import webdriver


class Base():

    def setup(self):
        # browser = os.getenv("browser")
        # if browser == 'chrome':
        #     self.driver = webdriver.Chrome()
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)  #隐式等待，全局的
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()


