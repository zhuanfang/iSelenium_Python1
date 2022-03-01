from appium.webdriver.common.mobileby import MobileBy

from app.page.basepage import BasePage
from app.page.editinfo import EditInfo


class DelInfo(BasePage):
    del_dian = (MobileBy.ID, "com.tencent.wework:id/iga")
    def delinfo(self):
        self.find_and_click(self.del_dian)
        return EditInfo(self.driver)