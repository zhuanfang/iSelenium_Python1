import requests

from test_web.api.util import Util
from test_web.api.wework import WeWork


class TestWework():
    def test_get(self):
        print(WeWork().test_get("chutian1"))


    def test_create(self):
        print(WeWork().test_create("daiyu1","18812345678","daiyu"))


    def test_update(self):
        print(WeWork().test_update("daiyu1","黛玉1"))


    def test_delete(self):
        print(WeWork().test_delete("daiyu1"))


    # def test_session(self):
    #     s = requests.session()
    #     s.params = {"access_token":Util().get_token()}
    #     res = s.get("")
    #     print(res.json())
