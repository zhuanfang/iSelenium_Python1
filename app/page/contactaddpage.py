import time

from appium.webdriver.common.mobileby import MobileBy

from app.page.basepage import BasePage


class ContactAddPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver

    add_name = (MobileBy.XPATH,
                "//*[contains(@text,'姓名')]/../*[@text='必填']")
    add_gender = (MobileBy.XPATH,
                "//*[contains(@text,'性别')]/..//*[@text='男']")
    add_male = (MobileBy.XPATH, "//*[@text='男']")
    add_female = (MobileBy.XPATH, "//*[@text='女']")
    add_phonenum = (MobileBy.ID, "com.tencent.wework:id/fwi")
    add_save = (MobileBy.ID, "com.tencent.wework:id/aj_")


    def set_name(self,name):
        #self.driver.find_element_by_xpath("//*[contains(@text,'姓名')]/../*[@text='必填']").send_keys(name)
        self.find_and_sendkeys(self.add_name,name)
        return self

    def set_gender(self,gender):
        # self.driver.find_element(MobileBy.XPATH,
        #                          "//*[contains(@text,'性别')]/..//*[@text='男']").click()
        self.find_and_click(self.add_gender)
        print("--下一步带年纪性别--", gender)
        time.sleep(2)
        if gender == '男':
            #self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
            self.find_and_click(self.add_male)
        else:
            #self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
            self.find_and_click(self.add_female)
            time.sleep(2)

        return self

    def set_phonenum(self,phonenum):
        #self.driver.find_element_by_id("com.tencent.wework:id/fwi").send_keys(phonenum)
        self.find_and_sendkeys(self.add_phonenum,phonenum)
        return self

    def click_save(self):
        from app.page.addmemberpage import AddMemberPage
        #self.driver.find_element_by_id("com.tencent.wework:id/aj_").click()
        self.find_and_click(self.add_save)
        return AddMemberPage(self.driver)