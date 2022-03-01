import yaml

from web_label.api.baseapi import BaseApi
from web_label.api.util import Util


class Label(BaseApi):
    def __init__(self):
        self.token = Util().get_token()
        self.params["token"] = self.token
        with open("C:/python-system/iSelenium_Python1/web_label/api/label.yaml",encoding="utf-8") as f:
            self.data = yaml.load(f)

    def test_create(self,name,parentid,order,id):
        self.params["name"] = name
        self.params["parentid"] = parentid
        self.params["order"] = order
        self.params["id"] = id
        return self.send(self.data["create"])

    def test_get(self,id):
        self.params["id"] = id
        return self.send(self.data["get"])

    def test_update(self,id,name):
        self.params["id"] = id
        self.params["name"] = name
        return self.send(self.data["update"])

    def test_delete(self,id):
        self.params["id"] = id
        return self.send(self.data["delete"])


