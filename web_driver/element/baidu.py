from time import  sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

"""
1.打开百度
2.输入内容“霍格沃兹测试学院”并点击
2.查找需要的链接
"""
class Test_demo():
    def sutup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()
    def teardown(self):
        self.driver.quit()

    def test_baidu(self):
        # self.driver.get("https://www.baidu.com")
        # self.driver.find_element_by_id("kw").send_keys("霍格沃茨测试学院")
        # self.driver.find_element_by_xpath("//*[@id='su']").click()
        # self.driver.find_element_by_xpath("//*[@id='2']/h3").click()
        # WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(By.XPATH,'//*[@class = "table_heading"]'))

        self.driver.get("https://sahitest.com/demo/clicks.htm")
        a_click = self.driver.find_element_by_xpath("//input[@value='click me']")
        b_doubleclick = self.driver.find_element_by_xpath("//input[@value= 'dbl click me']")
        c_righhtclick = self.driver.find_element_by_xpath("//input[@value = 'right click me']")
        action = ActionChains(self.driver)
        action.click(a_click)
        sleep(3)
        action.context_click(c_righhtclick)
        sleep(4)
        action.double_click(b_doubleclick)
        action.perform()
        sleep(5)

    def test_hadles(self):
        """
        打开百度页面
        点击登录
        弹框中点击“立即注册”，输入用户名和账号
        返回刚才的登录页，点击登录
        输入用户名和密码，点击登录
        :return:
        """
        self.driver.get("https://baidu.com")
        self.driver.find_element_by_link_text("登录").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        self.driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_11__regLink']").click()
        print(self.driver.current_window_handle)
        print(self.driver.window_handles)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

        self.driver.find_element_by_id("TANGRAM__PSP_4__userName").send_keys("liu")
        self.driver.find_element_by_id("TANGRAM__PSP_4__phone").send_keys("password")
        sleep(4)
        self.driver.switch_to.window(windows[0])
        self.driver.find_element_by_id("TANGRAM__PSP_11__userName").send_keys("liu")
        self.driver.find_element_by_id("TANGRAM__PSP_11__password").send_keys("password")
        sleep(4)

    def test_frame(self):
        """
        frame,拖拽
        :return:
        """
        self.driver.get("http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable")
        self.driver.switch_to.frame("iframeResult")
        print(self.driver.find_element_by_id("draggable").text)
        self.driver.switch_to.default_content()
        sleep(3)
        print(self.driver.find_element_by_id('submitBTN').text)


    # 执行 browser=Chrome pytest baidu.py
    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        #time_element = self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly')")

