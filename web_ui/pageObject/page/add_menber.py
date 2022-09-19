import time

from selenium.webdriver.common.by import By

from web_ui.pageObject.page.contact import Contact
from web_ui.pageObject.page.po_base import Base
import random


# import bson


class AddMember(Base):
    # 将定位提取出来
    _location_username = (By.ID, 'username')
    _location_acctid = (By.ID, 'memberAdd_acctid')
    _location_phone = (By.ID, 'memberAdd_phone')

    def add_member(self):
        name = random.randint(100, 900)
        id = int(time.time())
        # create_id = bson.ObjectId()#创建id，例631afa8c8ffaed5625859b2f

        # (*self._location_username)  *：解元组操作
        self.find(*self._location_username).send_keys(f"hms{name}")
        self.find(self._location_acctid).send_keys(id)

        self.find(*self._location_phone).send_keys(f"18899998{name}")
        self.find(By.CSS_SELECTOR, '.member_colRight_operationBar:nth-child(1)>a:nth-child(2)').click()

        time.sleep(3)

        return Contact(self.driver)

    def add_member_fail(self, acctid, phone):
        self.driver.find_element(By.ID, 'username').send_keys(f"hms222")
        self.driver.find_element(By.ID, 'memberAdd_acctid').send_keys(acctid)

        self.driver.find_element(By.ID, 'memberAdd_phone').send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, '.member_colRight_operationBar:nth-child(1)>a:nth-child(2)').click()

        error_tip_list = self.error_tips()

        return error_tip_list

    def error_tips(self):
        error_tips = self.driver.find_elements(By.CSS_SELECTOR, '.ww_inputWithTips_tips')

        error_tip_list = [i.text for i in error_tips]

        # for error_tip in error_tips:
        #     error_tip_list.append(error_tip.text)

        return error_tip_list
