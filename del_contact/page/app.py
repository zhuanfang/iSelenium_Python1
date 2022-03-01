from appium import webdriver

from app.page.basepage import BasePage
from app.page.mainpage import MainPage

"""
存放 app 常用的方法，比如 启动 重启 停止app，进入首页
"""
class App(BasePage):
    def start(self):
        """
        启动 app
        :return:
        """
        if self.driver == None:
            # 第一次调用start()方法的时候 driver为 None
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '6.0'
            desired_caps['deviceName'] = '127.0.0.1:7555'
            desired_caps['appPackage'] = 'com.tencent.wework'
            desired_caps['appActivity'] = '.launch.WwMainActivity'
            desired_caps['noReset'] = 'true'
            # desired_caps['dontStopAppOnReset '] = 'true'
            desired_caps['skipDeviceInitialization'] = 'true'
            desired_caps['skipServerInstallation'] = 'true'
            desired_caps['settings[waitForIdleTimeout]'] = 0
            # desired_caps['unicodeKeyBoard'] = 'true'
            # desired_caps['resetKeyBoard'] = 'true'
            # 建立与server的连接，初始化一个driver 创建session 返回一个sessionid
            self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        else:
            # launch_app()  --启动页面，这个方法不需要传入任何参数，会自动启动 deaired[]apppackage+appactivity
            # start_activity(packagename,activityname)
            self.driver.launch_app()
        self.driver.implicitly_wait(5)
        return self

    def restart(self):
        self.driver.close()
        self.driver.launch_app() # 重启app
        return self

    def stop(self):

        self.driver.quit()

    def goto_main(self):
        """
        进入 首页
        """
        return MainPage(self.driver)