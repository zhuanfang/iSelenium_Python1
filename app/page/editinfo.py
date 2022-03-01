from appium.webdriver.common.mobileby import MobileBy

from app.page.basepage import BasePage
from app.page.delelement import DelElement


class EditInfo(BasePage):
    edit_contact = (MobileBy.ID, "com.tencent.wework:id/bct")
    def editinfo(self):
        self.find_and_click(self.edit_contact)
        return DelElement(self.driver)