import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

#ActionChains 只能模拟pc端 鼠标和键盘的操作

class Test_ActionChains():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)  #隐式等待，全局的
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip    #忽略该case
    def test_click(self):

        self.driver.get("https://www.baidu.com/")
        elements =  self.driver.find_element(By.ID,'kw')

        action = ActionChains(self.driver)
        action.click(elements)  #点击
        action.context_click(elements)  #鼠标右键点击
        action.double_click(elements)  #双击
        # action.click_and_hold(elements) #拖动
        action.perform()  #执行

    @pytest.mark.skip    #忽略该case
    def test_movetoelement(self):
        self.driver.get("https://www.baidu.com/")
        ele = self.driver.find_element(By.LINK_TEXT,'设置')

        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()

    @pytest.mark.skip  # 忽略该case
    def test_dragdrop(self):
        self.driver.get("https://www.baidu.com/")
        el =  self.driver.find_element(By.ID,'kw')
        el1 =  self.driver.find_element(By.ID,'su')

        action = ActionChains(self.driver)
        #拖动a到b
        #方式一：
        # action.drag_and_drop(el,el1).perform()
        #方式二：
        # action.click_and_hold(el).release(el1).perform()
        #方式三：
        action.click_and_hold(el).move_to_element(el1).release().perform()

    def test_keys(self):
        self.driver.get("https://www.baidu.com/")
        e =  self.driver.find_element(By.ID,'kw')
        e.click()

        action = ActionChains(self.driver)
        action.send_keys('hms').pause(1)  #pause(1)暂停1秒
        action.send_keys(Keys.SPACE).pause(1)  #Keys.SPACE 点击空格
        action.send_keys('qqq').pause(1)
        action.send_keys(Keys.BACK_SPACE).pause(1)  #Keys.BACK_SPACE  点击back
        action.perform()
