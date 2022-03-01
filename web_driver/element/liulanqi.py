import json
from time import sleep

from selenium import webdriver

class Test_temp():
    def setup_method(self,method):
        chrome_arg = webdriver.ChromeOptions()
        chrome_arg.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome() #options=chrome_arg
        self.driver.implicitly_wait(4)
        self.vars = {}
    def teardown_method(self,method):
        self.driver.quit()

    def test_tmp(self):
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.find_element_by_xpath("//*[@class='index_top_operation_loginBtn']").click()
        self.driver.find_element_by_id("menu_contacts").click()

    def test_cookies(self):
        # cookies = self.driver.get_cookies() #获取cookies
        # print(cookies)
        """
        携带cookies，直接登录
        """
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False, 'value': 'a3637885'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False, 'value': 'w43IWvkVZl4HC7VCE89xcwUSmKGyimgbaNXjYM0EwUofO-74rcupbhijjTE_nHmBKIvsroIy8xIE7WxhYA53wyDdbUWYj1rzXpTn5_KrwOKTarnXFnQoB4ZOUFuzo1WNWyKz6jR_2uNNiRiviCLZmRpjpGKRZtjj0YtWoN7hL3PiQqEGIRH4CDJzrUKhHxjhs6mlczLPkI4Ro0HnjwtWnBo0Kz4l6shy0rUNIxVh0WozpeUdlOzZFUcpQhPEo2ieZOxxAB7rFzBT54C-ztc9JA'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False, 'value': 'wbUzNl2Mt7LwcFzkskdPD0sybuQMFuXBLikmItsFkTzsI1wJZialB0PulVuaprj9'}, {'domain': '.qq.com', 'httpOnly': False, 'name': 'pgv_info', 'path': '/', 'secure': False, 'value': 'ssid=s307887083'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.cs_ind', 'path': '/', 'secure': False, 'value': ''}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False, 'value': '1688850899983137'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False, 'value': '1970324942161578'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False, 'value': '1688850899983137'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.logined', 'path': '/', 'secure': False, 'value': 'true'}, {'domain': '.qq.com', 'expiry': 1639408716, 'httpOnly': False, 'name': '_gid', 'path': '/', 'secure': False, 'value': 'GA1.2.1737724152.1639306610'}, {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1639322291'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False, 'value': '30606132321527312'}, {'domain': '.qq.com', 'expiry': 1954061013, 'httpOnly': False, 'name': 'tvfe_boss_uuid', 'path': '/', 'secure': False, 'value': 'dd1cd331ab86fa3f'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False, 'value': '1'}, {'domain': '.work.weixin.qq.com', 'expiry': 1670858291, 'httpOnly': False, 'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/', 'secure': False, 'value': '1639306610,1639307581,1639307824,1639308329'}, {'domain': '.qq.com', 'expiry': 2147385600, 'httpOnly': False, 'name': 'pgv_pvid', 'path': '/', 'secure': False, 'value': '7973428356'}, {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False, 'value': 'direct'}, {'domain': '.qq.com', 'expiry': 2147483648, 'httpOnly': False, 'name': 'RK', 'path': '/', 'secure': False, 'value': 'zNYBLwjXPb'}, {'domain': '.qq.com', 'expiry': 2147483647, 'httpOnly': False, 'name': 'ptcz', 'path': '/', 'secure': False, 'value': 'f8b405f7899fad3608e973c81830e364440cd471d727c32fb8df21daeeccde16'}, {'domain': '.qq.com', 'expiry': 1920985242, 'httpOnly': False, 'name': 'pac_uid', 'path': '/', 'secure': False, 'value': '0_913698f0d2b42'}, {'domain': '.work.weixin.qq.com', 'expiry': 1641914318, 'httpOnly': False, 'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}, {'domain': '.work.weixin.qq.com', 'expiry': 1667140247, 'httpOnly': False, 'name': 'wwrtx.c_gdpr', 'path': '/', 'secure': False, 'value': '0'}, {'domain': '.qq.com', 'expiry': 1702394316, 'httpOnly': False, 'name': '_ga', 'path': '/', 'secure': False, 'value': 'GA1.2.1669102873.1603812839'}]
        # for i in cookies:
        #     self.driver.add_cookie(i)
        # self.driver.refresh()
        # sleep(5)

        #c存入cookies
        # cookies = self.driver.get_cookies()
        # with open("tmp.txt","w",encoding="utf-8") as f:
        #     f.write(json.dumps(cookies))

        # 读取 cookies
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # with open("tmp.txt","r",encoding="utf-8") as f:
        #     cookies = json.load(f)
        # for i in cookies:
        #     self.driver.add_cookie(i)
        # self.driver.refresh()
        # sleep(5)




