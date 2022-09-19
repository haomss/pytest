import requests

from test_requests.page_req.base import Base


class Contact(Base):

    def create_member(self, userid: str, name: str, mobile: str, department: list, **kwargs):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/create"
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        data.update(kwargs)
        r = self.s.post(url=url, json=data)
        return r.json()

    def find_user_list_id(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/list_id"
        r = self.s.post(url=url)
        return r.json()["dept_user"]

    def update_member(self, userid: str, name: str, mobile: str, **kwargs):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/update"
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
        }
        data.update(kwargs)
        r = self.s.post(url=url, json=data)
        return r.json()

    def delete_member(self, userid):
        url = "https://qyapi.weixin.qq.com/cgi-bin/user/delete"
        params = {"userid": userid}
        r = self.s.get(url=url, params=params)
        return r.json()
