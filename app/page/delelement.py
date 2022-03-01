from appium.webdriver.common.mobileby import MobileBy

from app.page.basepage import BasePage
from app.page.delconfirm import DelConfirm


class DelElement(BasePage):
    delelement1 = (MobileBy.ID, "com.tencent.wework:id/esd")
    def delelement(self):
        self.find_and_click(self.delelement1)
        return DelConfirm(self.driver)