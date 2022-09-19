from time import sleep

from selenium.webdriver.common.by import By

from web_ui.base import Base


class TestUpload(Base):
    def test_upload(self):
        self.driver.get("https://image.baidu.com/")
        self.driver.find_element(By.XPATH,'//*[@id="sttb"]/img[1]').click()
        self.driver.find_element(By.ID,"stfile").send_keys("/Users/haomengshan/PycharmProjects/untitled1/web_ui/img/bonui.jpeg")
        sleep(3)

# 有input属性的可以直接用send_keys("/path")上传文件



