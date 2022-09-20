from time import sleep

import pytest
import yaml
from selenium import webdriver

from web_ui.pageObject.page.mainPage import mainPage
from web_ui.pageObject.page.po_base import Base


class Testwx():

    def setup_class(self):
        self.main = mainPage()

    def test_add_mem_in_index(self):
        res = self.main.goto_addmember().add_member().get_mem_list()

        assert "hms333" in res

    @pytest.mark.parametrize("acctid,phone,expect_res", [("yyy", "13344445555", "该帐号已被“yyy”占有"),
                                                         ("xxx", "18301306637", "该手机已被“郝孟珊”占有")])
    # case1：acctid重复
    # case2：phone重复
    def test_add_mem_fail(self, acctid, phone, expect_res):
        # self.main.goto_index()

        res = self.main.goto_addmember().add_member_fail(acctid, phone)

        assert expect_res in res

    def test_add_mem_in_contact(self):
        # self.main.goto_index()

        res = self.main.goto_contact().contact_add_mem().add_member().get_mem_list()

        assert "hms333" in res

    def teardown(self):
        self.main.goto_index()

    def teardown_class(self):
        self.main.quit()
