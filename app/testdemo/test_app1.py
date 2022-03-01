import time

import pytest
from appium import webdriver

from appium.webdriver.common.touch_action import TouchAction

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy


class TestWX():
    def setup(self):
        desired_caps={}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.eastmoney.android.berlin'
        desired_caps['appActivity'] = 'com.eastmoney.android.module.launcher.internal.home.HomeActivity'
        desired_caps['noReset'] = 'true'
        desired_caps['dontStopAppOnReset '] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        self.driver.implicitly_wait(5)
    # def teardown(self):
        #self.driver.quit()

    # @pytest.mark.parametrize('search,type',[
    #     ('ali','阿里巴巴'),
    #     ('300059','东方财富')
    # ])
    # # 参数化
    # def test_wx(self,search,type):
    #     print("企业微信")
    #     self.driver.find_element_by_id("com.eastmoney.android.berlin:id/tv_ad_text") .click()
    #     self.driver.find_element_by_id("com.eastmoney.android.berlin:id/et_search").send_keys(search)
    #     self.driver.find_element_by_xpath(f"//*[@text='{type}']").click()
    #
    #     time.sleep(4)

    # #查找元素是否可用
    # def test_atrri(self):
    #     ele = self.driver.find_element_by_id("com.eastmoney.android.berlin:id/tv_ad_text")
    #     print(ele.text)
    #     print(ele.location)
    #     print(ele.size)
    #     ele_enabled = ele.is_enabled()
    #     if ele_enabled is True:
    #         ele.click()
    #         alibab_element = self.driver.find_element_by_id("com.eastmoney.android.berlin:id/et_search").send_keys('ali')
    #         self.driver.find_element_by_xpath("//*[@text='阿里巴巴']")
    #         alibaba_display = alibab_element.is_displayed()
    #         alibaba_display = alibab_element.get_attribute("displayed")
    #         print(alibaba_display)
    #         if alibaba_display == 'true':
    #             print("搜索成功")
    #         else:
    #             print("搜索失败")
    #     else:
    #         print("搜索框不可见")

    # 显示等待使用
    def test_wait(self):
        self.driver.find_element_by_id("com.eastmoney.android.berlin:id/tv_ad_text").click()
        self.driver.find_element_by_id("com.eastmoney.android.berlin:id/et_search").send_keys("ali")
        element = (MobileBy.XPATH,"//*[@text='阿里巴巴']")
        ele = WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(element))
        #ele1 = WebDriverWait(self.driver,10).until(lambda x:x.find_element(*element))
        print(ele.text)






    if __name__=='__main__':
        pytest.main()