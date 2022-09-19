import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver import TouchActions #selenium版本太高，4以下的可以
from selenium.webdriver.common.by import By

#TouchAction 也可模拟移动端操作

class Test_TouchAction():

    def setup(self):

        #解决这个报错：selenium.common.exceptions.WebDriverException: Message: unknown command: Cannot call non W3C standard command while in W3C mode
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)  #隐式等待，全局的
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    def test_scorllbutton(self):
        self.driver.get("https://www.baidu.com/")
        elements = self.driver.find_element(By.ID, 'kw')
        elements.send_keys('hms')
        elements1 = self.driver.find_element(By.ID, 'su')

        action = TouchActions(self.driver)
        action.tap(elements1) #点击
        # action.perform()

        action.scroll_from_element(elements,0,10000).perform()  #滑动到底部