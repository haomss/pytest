from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Test_hms():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)  #隐式等待，全局的

    def teardown(self):
        self.driver.quit()

    def test_daidu(self):

        self.driver.get("https://www.baidu.com/")
        #显式等待，方式一：until（）中需要传入一个函数，可以自定义一个wait（x），必须有一个参数；方式二：如下
        WebDriverWait(self.driver,10).until(expected_conditions.presence_of_all_elements_located((By.XPATH,'//*[@id="s-hotsearch-wrapper"]/div/a[1]/div/i[1]')))

        self.driver.find_element(By.ID,"kw").send_keys("hms")

        sleep(3)#直接等待，不推荐
        self.driver.find_element(By.ID,"su").click()

#xpath定位  $x('//*[@id="s-hotsearch-wrapper"]/div/a[1]/div/i[1]')
#  /子目录   //子孙目录   @属性    /div/a[1] div下第一个a元素     /div/a[last()] div下倒数第一个a元素，[last()-1]为倒数第二个    *全部元素   .当前目录   ..上层目录

#css selector定位  $('#kw')
#  #id属性     [name = wd]name属性    .class属性    空格：子孙元素    >子目录    =兄弟目录   a:nth-child(2) a的父元素的第二个子元素    a:nth-last-child(1) a的父元素的倒数第一个元素




