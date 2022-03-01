from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class Test_wework():
    def setup(self):
        chrome_arg=webdriver.ChromeOptions()
        chrome_arg.debugger_address="127.0.0.1:2333"
        self.driver=webdriver.Chrome(options=chrome_arg)
        #self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_work(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(2)
        self.driver.find_element_by_xpath("//*[@id='menu_contacts']").click()
        sleep(2)
        def wait_name(driver):
            driver.find_elements_by_xpath("//*[@class='qui_btn ww_btn js_add_member']")[1].click()
            eles = driver.find_elements_by_xpath("//*[@class='qui_btn ww_btn ww_btn_Blue js_btn_continue']")
            return len(eles)>0
        WebDriverWait(self.driver,10).until(wait_name)
        self.driver.find_element_by_id("username").send_keys("fang1")
        self.driver.find_element_by_id("memberAdd_acctid").send_keys("13")
        self.driver.find_element_by_id("memberAdd_phone").send_keys("13911111103")
        self.driver.find_element_by_xpath("//*[@class='qui_btn ww_btn js_btn_save']").click()
