
# corpid = "wwdae6409305b8bd0c"
# corpsecret = "rsOHnc_DnUXkca3XIfydIht08uwsLje4aLUm95WSMYc"

import requests

class Test_Demo():
    def setup(self):
        self.token = self.get_token()

    def get_token(self):
        corpid = "wwdae6409305b8bd0c"
        corpsecret = "rsOHnc_DnUXkca3XIfydIht08uwsLje4aLUm95WSMYc"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(url)
        token = r.json()['access_token']
        print(token)
        return token

    def test_create_number(self):
        create_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={self.token}"
        param = {
            "userid": "chutian6",
            "name": "雏田6",
            "mobile": "+86 13812300006",
            'department': [1]
        }
        r = requests.post(create_url,json=param)
        print(r.json())
        assert "created" == r.json()["errmsg"]

    def test_get(self):
        get_url = f'https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={self.token}&userid=chutian6'
        r = requests.get(get_url)
        print(r.json())
        assert  "雏田6" == r.json()['name']

    def test_update(self):
        update_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={self.token}"
        param = {
            "userid": "chutian6",
            "name": "小英"
        }
        r = requests.post(update_url,json=param)
        print(r.json())
        assert "updated" == r.json()["errmsg"]

    def test_delete(self):
        USERID="chutian6"
        delete_url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={self.token}&userid={USERID}"
        r = requests.get(delete_url)
        print(r.json())
        assert "deleted" == r.json()["errmsg"]
