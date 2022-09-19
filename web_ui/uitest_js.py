from time import sleep

from web_ui.base import Base


#用js修改时间，首先定位到时间元素，然后去掉元素的onlyread属性，最后赋值
class TestJs(Base):
    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        time_element = self.driver.execute_script('a=document.getElementById("train_date"),a.removeAttribute("onlyread"),a.value="2022-12-01"')
        sleep(2)


# 可用execute_script()执行js代码块，如果要返回结果，需要加return，例如：e = self.driver.execute_script(return '{js代码块}')