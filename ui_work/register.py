class RegisterPage():
    def __init__(self,driver):
        self.driver=driver

    def register(self):
        self.driver.find_element_by_id("corp_name").send_keys("输入企业名称")