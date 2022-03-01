import requests


class Util:
    def get_token(self):
        request_patams = {
            "corpid" : "wwdae6409305b8bd0c",
            "corpsecret" : "rsOHnc_DnUXkca3XIfydIht08uwsLje4aLUm95WSMYc"
        }
        r = requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            params = request_patams
        )
        return r.json()["access_token"]