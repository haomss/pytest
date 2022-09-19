import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By

from web_ui.pageObject.page.add_menber import AddMember
from web_ui.pageObject.page.contact import Contact
from web_ui.pageObject.page.po_base import Base


class TestIndex():

    def setup(self):
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")


    def testgoto_addmember(self):
        self.driver = webdriver.Chrome()

        with open("potestdata.yaml", encoding="UTF-8") as f:
            yaml_data = yaml.safe_load(f)
            for cookie in yaml_data:
                self.driver.add_cookie(cookie)

                self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

        self.driver.find_element(By.CSS_SELECTOR,'.ww_indexImg_AddMember').click()

    def teardown(self):
        self.driver.quit()

