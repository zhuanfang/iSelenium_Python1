import random

import pytest
import requests
import random


class Test_departmen():

    def setup(self):
        self.token = self.get_token()


    def get_token(self):
        corpid = "wwdae6409305b8bd0c"
        corpsecret = "rsOHnc_DnUXkca3XIfydIht08uwsLje4aLUm95WSMYc"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(url)
        print(r)
        token = r.json()['access_token']
        print(token)
        return token

    # @pytest.mark.parametrize("name,parentid,order,id", [("hub测试",1,1,11),
    #                                                     ("tra测试",1,1,12),
    #                                                     ], ids=["test1","test2"])

    # @pytest.mark.parametrize("name,parentid,order,id",[(
    #    "hub测试"+str(x),
    #     1,
    #     1,
    #     5+x)for x in range(5)
    # ])

    @pytest.mark.parametrize("name,parentid,order,id",[(
        "SGP测试"+str(random.randint(5,20)),
        1,
        1,
        10+random.randint(1,15) )for x in range(5)
    ])
    def test_create(self,name,parentid,order,id):

        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={self.token}"
        params = {
            "name": name,
            "parentid": parentid,
            "order": order,
            "id":id
        }
        r = requests.post(url,json = params)
        print(r.json())

    def test_get(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={self.token}&id=4"
        r = requests.get(url)
        print(r.json())

    def test_update(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={self.token}"
        params ={
            "id": 4,
            "name": "HUB研发中心"}
        r = requests.post(url,json = params)
        print(r.json())

    def test_delete(self):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={self.token}&id=4"
        r = requests.get(url)
        print(r.json())







a = "{s:1, b : 2}"
