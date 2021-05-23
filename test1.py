import time

import requests
from selenium.webdriver.chrome import webdriver


class TestHogwarts():
    def test(self):
        self.driver = webdriver.WebDriver()
        self.driver.get("http://www.baidu.com")
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    # def teardown(self):
    #     time.sleep(2)
    #     self.driver.quit()

