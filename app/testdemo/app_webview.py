from time import sleep

from appium import webdriver



class TestBrowser():
    def setup(self):
        des_caps={
            'platformName':'android',
            'platformVersion':'6.0',
            #'browserName':'Browser',
            'appPackage':'io.appium.android.apis',
            'appActivity':'io.appium.android.apis.view.WebView1',
            'noReset':True,
            'deviceName':'127.0.0.1:7555',
            'chromedriverExecutable':'C:/files_liu/webdriver/chromedriver'

        }
        self.driver = webdriver.Remote('127.0.0.1:7555/wb/hub',des_caps)
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_webview(self):
        self.driver.find_element_by_id("views").click()
        webview = 'WebView'
        print(self.driver.contexts)
        sleep(5)