import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

"""
BasePage：存放一些基本的方法，如 初始化 driver，find查找元素
          存放公共方法，其他类需要可直接继承
driver：存在则直接复用，不存在 再去创建
        功能 --初始化设备+与server建立连接
"""
class BasePage():

    logging.basicConfig(level=logging.INFO)  # --添加日志

    # driver：WebDriver=None  --设置默认值为 None
    def __init__(self,driver:WebDriver=None):
        self.driver = driver


    def find(self,locator):
        logging.info(f'find:{locator}')
        return self.driver.find_element(*locator)

    def find_and_click(self,locator):
        logging.info(f'click:{locator}')
        self.find(locator).click()

    def find_and_sendkeys(self,locator,text):
        logging.info(f'send_keys:{text}')
        self.find(locator).send_keys(text)

    def find_by_scroll(self,text):
        logging.info(f'find_by_scroll:{text}')
        return self.driver.find_element(
            MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable'
                                          '(new UiSelector().'
                                          'scrollable(true).'
                                          'instance(0)).'
                                          'scrollIntoView('
                                          'new UiSelector().'
                                          f'text("{text}").instance(0));')
    def webdriverwait(self,locator,timeout=10):
        logging.info(f'webdriverwait:{locator},{timeout}')
        return  WebDriverWait(self.driver,timeout).until(lambda x:x.find_element(*locator))

    def back(self,num = 1):
        logging.info(f'back:{num}')
        for i in range(num):
            self.driver.back()


