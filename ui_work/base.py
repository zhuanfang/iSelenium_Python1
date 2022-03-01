from selenium import webdriver

from ui_work.login import LoginPage
from ui_work.register import RegisterPage


class Base():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(4)
        self.driver.get("")
    def goto_login(self):
        self.driver.find_element_by_xpath("//*[@class='index_top_operation_loginBtn']").click()
        return RegisterPage(self.driver)
    def goto_register(self):
        self.driver.find_element_by_xpath("//*[@class='index_head_info_pCDownloadBtn']")
        return LoginPage(self.driver)

