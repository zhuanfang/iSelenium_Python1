
"""
主页面
"""
from appium.webdriver.common.mobileby import MobileBy
from app.page.basepage import BasePage
from app.page.contactlistpage import ContactListPage


class MainPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver

    contactlist_ele = (MobileBy.XPATH, "//*[@text='通讯录']")

    def goto_contactListPage(self):
        """
        进入到通讯录
        :return:
        """
        # self.driver.find_element_by_xpath("//*[@text='通讯录']").click()
        self.find_and_click(self.contactlist_ele)
        return ContactListPage(self.driver)

    def goto_contactwork(self):
        """
        进入工作台
        :return:
        """
        pass