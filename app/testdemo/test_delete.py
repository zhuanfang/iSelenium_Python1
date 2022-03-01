import time

import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

with open("../testdemo/deletecontact.yaml","r",encoding='UTF-8') as f:
    data = yaml.safe_load(f)


class TestDelete():

    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.WwMainActivity'
        desired_caps['noReset'] = 'true'
        desired_caps['dontStopAppOnReset '] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['skipServerInstallation'] = 'true'
        desired_caps['settings[waitForIdleTimeout]'] = 0
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        #self.driver = webdriver.Remote("http://127.0.0.1:4723/wb/hub", desired_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()
    @pytest.mark.parametrize('name',data)
    def test_delete(self,name):
        self.driver.find_element_by_xpath("//*[@text='通讯录']").click()
        # 点击搜索框
        self.driver.find_element_by_id("com.tencent.wework:id/igk").click()
        # 输入名字
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gy9").send_keys(name)
        time.sleep(3)
        elelist = self.driver.find_elements_by_xpath(f"//*[contains(@text,'{name}')]")
        if len(elelist) < 2:
            print("没有找到联系人")
            return
        elelist[2].click()

        # 点击 三个点
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/iga").click()
        # 点击 编辑信息
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/bct").click()
        # 点击 删除
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/esd").click()
        #二次确认页 点击 确认
        self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/bpc").click()
        time.sleep(2)
        # 断言 验证删除成功
        elelist2 = self.driver.find_elements(MobileBy.XPATH, f"//*[contains(@text, '{name}')]")
        assert len(elelist2) == len(elelist) - 1
        time.sleep(2)
