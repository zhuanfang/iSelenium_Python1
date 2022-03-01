from appium.webdriver.common.mobileby import MobileBy

from app.page.basepage import BasePage



class DelConfirm(BasePage):
    delconfirm1 = (MobileBy.ID, "com.tencent.wework:id/bpc")
    def delconfirm(self):
        self.find_and_click(self.delconfirm1)
        from app.page.contactlistpage import ContactListPage
        return ContactListPage(self.driver)