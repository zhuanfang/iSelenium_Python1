import yaml

from test_web.api.baseapi import BaseApi
from test_web.api.util import Util


class WeWork(BaseApi):
    def __init__(self):
        self.token = Util().get_token()
        self.params["token"] = self.token
        with open("../api/wework.yaml", encoding="utf-8") as f:
            self.data = yaml.load(f)

    def test_create(self,userid,mobile,name="柯南",department=None):
        if department is None:
            department = "1"
        self.params["userid"]=userid
        self.params["mobile"]=mobile
        self.params["name"]=name
        self.params["department"]=department
        return self.send(self.data["create"])

    def test_get(self,userid):
        self.params["userid"]=userid
        return self.send(self.data["get"])

    def test_update(self,userid,name="柯南"):
        self.params["name"]=name
        self.params["userid"]=userid
        return self.send(self.data["update"])

    def test_delete(self,userid):
        self.params["userid"]=userid
        return self.send(self.data["delete"])