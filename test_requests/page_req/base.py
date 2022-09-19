import requests
from requests import Session


class Base():
    def __init__(self):
        self.s = Session()
        self.corpid = "1970325985979472"
        self.corpsecret = "xROUb6KXVwNNTjAu2ZBEDfnro0hulyZwJCQVyKhMw9Y"

        self.s.params["access_token"] = self.get_token().get("access_token")  # 将token传入到session中，实现只建立一次链接

    def get_token(self, corpid=None, corpsecret=None):  # token有过期时间，可以用时间戳判断过期时间，重新获取
        if corpid == None:
            corpid = self.corpid
        if corpsecret == None:
            corpsecret = self.corpsecret
        params = {"corpid": corpid, "corpsecret": corpsecret}
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        r = requests.get(url=url, params=params)
        return r.json()
