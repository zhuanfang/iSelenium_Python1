import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestWX():
    def setup(self):
        desired_caps={}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'cn.kmob.screenfingermovelock'
        desired_caps['appActivity'] = 'com.samsung.ui.MainActivity'
        desired_caps['noReset'] = 'true'
        desired_caps['dontStopAppOnReset '] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(5)
    # def teardown(self):
        #self.driver.quit()

# 模拟触屏操作，如图案密码
    def test_taction11(self):
        action = TouchAction(self.driver)
        action.press(x=125,y=185).wait(10).move_to(x=355,y=185).wait(10).move_to(x=600,y=185).wait(10).move_to(x=600,y=415).wait(10).move_to(x=600,y=665).release().perform()
        window_rect = self.driver.get_window_rect()
        print(window_rect)
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width/2)
        y_start = int(height * 4/5)
        y_end = int(height * 1/5)
        action.press(x=x1,y=y_start).wait(10).move_to(x=x1,y=y_end).release().perform()


    if __name__=='__main__':
        pytest.main()