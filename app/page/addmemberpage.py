
"""
添加成员页
"""
from appium.webdriver.common.mobileby import MobileBy

from app.page.basepage import BasePage

class AddMemberPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver

    addmenual_ele = (MobileBy.ID, "com.tencent.wework:id/ipb")

    """
    手动输入添加
    """
    def add_menual(self):
        from app.page.contactaddpage import ContactAddPage
        # self.driver.find_element_by_id("com.tencent.wework:id/ipb").click()
        self.find_and_click(self.addmenual_ele)
        return ContactAddPage(self.driver)

    def get_toast(self):
        text = '成功'
        return text