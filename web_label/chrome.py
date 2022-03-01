from time import sleep

from selenium import webdriver


class Test_Demo():
    def test_chrome(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get("https://work.weixin.qq.com/wework_admin/register_wx?from=myhome")
        #self.driver.find_element_by_xpath("//*[@id='corp_name']").send_keys("企业名称")
        #self.driver.find_element_by_id("corp_name").send_keys("企业微信1")
        self.driver.find_element_by_css_selector("#corp_name").send_keys("企业微信2")
        self.driver.find_element_by_xpath("//*[@class='ww_btn_Dropdown_arrow']").click()
        self.driver.find_element_by_xpath("//*[@data-name='教育']").click()
        self.driver.find_element_by_xpath("//*[text()='学前教育']").click()
        self.driver.find_element_by_xpath("//*[@class='qui_btn ww_btn ww_btn_Big ww_btn_Block ww_btn_Dropdown']/spa[2]").click()
        #self.driver.find_element_by_xpath('//*[text()="选择员工规模"]/../span[2]').click()
        #self.driver.find_element_by_xpath('//*[text()="选择员工规模"]/following-sibling::span[1]').click()
        self.driver.find_element_by_xpath("//*[text()='51-100人']").click()


        sleep(3)
        self.driver.quit()