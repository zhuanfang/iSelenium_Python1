class LoginPage():
    def __init__(self,driver):
        self.driver = driver

    def scan(self):
        pass
    def goto_register(self):
        self.driver.find_element_by_xpath("//*[@class='login_registerBar_link']").click()
