from time import sleep

import pytest
import yaml
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

with open("../testdemo/addcontact.yaml",'r',encoding='utf-8') as f:
    data = yaml.safe_load(f)

class Test_AddMber():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.WwMainActivity'
        desired_caps['noReset'] = 'true'
        # desired_caps['dontStopAppOnReset '] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['skipServerInstallation'] = 'true'
        desired_caps['settings[waitForIdleTimeout]'] = 0

        # desired_caps['unicodeKeyBoard'] = 'true'
        # desired_caps['resetKeyBoard'] = 'true'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    # @pytest.mark.parametrize('name,gender,phonenum',[
    #     ('冰墩墩8','女','13800000015'),
    #     ('冰墩墩9','男','13800000016')
    # ])
    @pytest.mark.parametrize('name,gender,phonenum',data)
    def test_add(self,name,gender,phonenum):
        self.driver.find_element_by_xpath("//*[@text='通讯录']").click()

        # 滚动查询到 添加成功并点击
        self.driver.find_element(
            MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable'
                                          '(new UiSelector().'
                                          'scrollable(true).'
                                          'instance(0)).'
                                          'scrollIntoView('
                                          'new UiSelector().'
                                          'text("添加成员").instance(0));').click()
        # 点击 手动输入
        self.driver.find_element_by_id("com.tencent.wework:id/ipb").click()

        # 输入 姓名
        self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/../*[@text='必填']").send_keys(name)

        # 下拉选择性别
        self.driver.find_element(MobileBy.XPATH,
                                 "//*[contains(@text,'性别')]/..//*[@text='男']").click()
        print("--下一步带年纪性别--", gender)
        if gender == '男':
            self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        else:
            self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()

        # if gender == '男':
        #     self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
        # else:
        #     self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()



        # 输入 手机号
        self.driver.find_element_by_id("com.tencent.wework:id/fwi").send_keys(phonenum)

        # 点击 保存
        self.driver.find_element_by_id("com.tencent.wework:id/aj_").click()

        # 添加断言，toast提示通过text属性获取
        el = self.driver.find_element_by_xpath("//*[contains(@text,'添加成功')]").text
        assert "添加成功" in el

