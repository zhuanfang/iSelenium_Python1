import requests


class Util:
    def get_token(self):
        request_params = {
            "corpid" : "wwdae6409305b8bd0c",
            "corpsecret" : "rsOHnc_DnUXkca3XIfydIht08uwsLje4aLUm95WSMYc"}
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        r = requests.get(url,params=request_params)
        token = r.json()['access_token']
        return token