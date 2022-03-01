from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class Test_Daka():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.WwMainActivity'
        desired_caps['noReset'] = 'true'
        #desired_caps['dontStopAppOnReset '] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['skipServerInstallation'] = 'true'
        desired_caps['settings[waitForIdleTimeout]'] = 0

        # desired_caps['unicodeKeyBoard'] = 'true'
        # desired_caps['resetKeyBoard'] = 'true'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()

    def test_daka(self):
        self.driver.find_element_by_xpath("//*[@text='工作台']").click()
        #self.driver.find_element_by_xpath("//*[@text='打卡']").click()
        #滚动查询页面元素 --固定语句
        self.driver.find_element(
            MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable'
                                          '(new UiSelector().'
                                          'scrollable(true).'
                                          'instance(0)).'
                                          'scrollIntoView('
                                          'new UiSelector().'
                                          'text("打卡").instance(0));').click()
        self.driver.find_element_by_id("com.tencent.wework:id/i1x").click()
        self.driver.find_element_by_xpath("//*[contains(@text,'次外出')]").click()
        el = self.driver.find_element_by_id("com.tencent.wework:id/pu").text
        assert el in '外出打卡成功'


