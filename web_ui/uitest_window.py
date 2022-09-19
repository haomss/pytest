from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

from web_ui.base import Base

class TestWindow(Base):
    def test_window(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element(By.LINK_TEXT,'登录').click()

        print(self.driver.current_window_handle)  #打印当前窗口
        print(self.driver.window_handles) #打印所以窗口

        self.driver.find_element(By.LINK_TEXT,'立即注册').click()

        print(self.driver.current_window_handle)  #打印当前窗口
        print(self.driver.window_handles)  #打印所以窗口

        window = self.driver.window_handles
        self.driver.switch_to.window(window[-1]) #切换窗口
        self.driver.find_element(By.ID,'TANGRAM__PSP_4__userName').send_keys('username')
        self.driver.switch_to.window(window[0])  #切换窗口

        self.driver.find_element(By.ID,'TANGRAM__PSP_11__userName').send_keys('username')
        self.driver.find_element(By.ID,'TANGRAM__PSP_11__password').send_keys('password')
        sleep(3)


