import pytest

from test_requests.page_req.contact import Contact
import requests


class TestContact():

    def setup_class(self):
        self.contact = Contact()
        self.userid = "111111"
        self.name = "测试数据"

    @pytest.mark.parametrize("corpid,corpsecret,result", [(None, None, 0), (0, None, 40013), (None, 0, 40001)])
    def test_get_token(self, corpid, corpsecret, result):
        r = self.contact.get_token(corpid, corpsecret)
        assert r.get("errcode") == result

    def test_create_mem(self):
        mobile = "18899996667"
        department = [2]
        r = self.contact.create_member(userid=self.userid, name=self.name, mobile=mobile, department=department,
                                       alias="cesj")
        assert r.get("errcode") == 0
        try:
            mem_list_id = self.contact.find_user_list_id()
        finally:
            self.contact.delete_member(self.userid)

        assert self.userid in str(mem_list_id)

    def test_update_mem(self):
        self.contact.create_member(userid=self.userid, name=self.name, mobile="18899996667", department=[2],
                                   alias="cesj")
        change_mobile = "18899996660"
        self.contact.update_member(userid=self.userid, name=self.name, mobile=change_mobile)
        try:
            mem_list_id = self.contact.find_user_list_id()
        finally:
            self.contact.delete_member(self.userid)

        assert self.userid in str(mem_list_id)  # 因为查询接口被废弃，所以用查询接口断言；最好是用查询接口断言mobile字段是否=change_mobile

    def test_find_mem(self, userid=None):
        userid = "hms111"
        r = self.contact.find_user_list_id()
        assert userid in str(r)

    def test_delete_mem(self):
        userid = "hmss"
        r = self.contact.delete_member(userid)
