from time import sleep

from selenium import webdriver


class Test_demo11():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()

    def test_1(self):
        self.driver.get("https://www.12306.cn/index/")
        js_pha = "document.getElementById('train_date').readOnly = false;"
        self.driver.execute_script(js_pha)
        self.driver.execute_script("document.getElementById('train_date').value=2021-12-21")
        sleep(5)
    def test_2(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        element = self.driver.find_element_by_id("su").click()
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        sleep(4)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollTop=0)")