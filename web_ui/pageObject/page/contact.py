import time
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from web_ui.pageObject.page.po_base import Base


class Contact(Base):

    def contact_add_mem(self):
        # 如果出现循环导入的问题(most likely due to a circular import)，可以将导入放在方法中
        from web_ui.pageObject.page.add_menber import AddMember

        sleep(5)

        self.wait_click((By.CSS_SELECTOR, '.ww_operationBar:nth-child(1)>.js_add_member'))

        # WebDriverWait(self.driver,20).until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR,'.ww_operationBar:nth-child(1)>.js_add_member')))

        self.driver.find_element(By.CSS_SELECTOR, '.ww_operationBar:nth-child(1)>.js_add_member').click()

        return AddMember(self.driver)

    def get_mem_list(self):
        mem_list = self.driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_tr>td:nth-child(2)')
        mem_name_list = []

        for mem_name in mem_list:
            mem_name_list.append(mem_name.text)

        return mem_name_list
