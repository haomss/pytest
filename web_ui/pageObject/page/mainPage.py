import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

from web_ui.pageObject.page.add_menber import AddMember
from web_ui.pageObject.page.contact import Contact
from web_ui.pageObject.page.po_base import Base


class mainPage(Base):
    _location_gotomember = (By.CSS_SELECTOR, '.ww_indexImg_AddMember')

    def goto_addmember(self):

        self.driver.find_element(*self._location_gotomember).click()

        return AddMember(self.driver)

    def goto_contact(self):

        self.driver.find_element(By.ID, 'menu_contacts').click()

        return Contact(self.driver)

    def goto_index(self):

        self.driver.find_element(By.ID, 'menu_index').click()

        try:

            self.driver.find_element(By.CSS_SELECTOR, '.qui_dialog_foot>a:nth-child(2)').click()

        except selenium.common.exceptions.NoSuchElementException as e:

            print(e)
