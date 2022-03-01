
"""
通讯录列表
"""
import time

from appium.webdriver.common.mobileby import MobileBy

from app.page.addmemberpage import AddMemberPage
from app.page.basepage import BasePage
from app.page.delinfo import DelInfo

# name = "冰墩墩"
class ContactListPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver

    addmember_text = "添加成员"
    deletemumber = (MobileBy.ID, "com.tencent.wework:id/igk")
    deletename = (MobileBy.ID, "com.tencent.wework:id/gy9")


    def add_contact(self):
        """
        添加成员
        :return:
        """
        # self.driver.find_element(
        #     MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable'
        #                                   '(new UiSelector().'
        #                                   'scrollable(true).'
        #                                   'instance(0)).'
        #                                   'scrollIntoView('
        #                                   'new UiSelector().'
        #                                   'text("添加成员").instance(0));').click()
        self.find_by_scroll(self.addmember_text).click()

        return AddMemberPage(self.driver)

    # 删除联系人 --找到检索框
    def search_contact(self):
        self.find_and_click(self.deletemumber)
        return self

    def send_contact(self,text):
        self.find_and_sendkeys(self.deletename,text)
        time.sleep(3)
        return self

    def click_contact(self):
        # self.webdriverwait(MobileBy.XPATH, "//*[contains(@text,'冰墩墩')]")
        elelist = self.driver.find_elements_by_xpath("//*[contains(@text,'冰墩墩')]")

        if len(elelist) < 2:
            print("没有找到联系人")
            return
        elelist[1].click()
        return DelInfo(self.driver)
