from API_UI_TestFramework.pages.main import Main
from API_UI_TestFramework.pages.base_page import BasePage
from appium import webdriver


class App(BasePage):
    def start(self):
        if self._driver == None:
            # 连接设备并打开应用
            desired_caps = {
                "platformName": "android",
                "platformVersion": "11.0",
                "deviceName": "72973146",
                "appPackage": "com.tencent.wework",
                "appActivity": ".launch.LaunchSplashActivity",
                "dontStopAppOnReset": False,
                "unicodeKeyBoard": True,
                "resetKeyboard": True,
                "noReset": True,

            }
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        else:
            self._driver.launch_app()
        self._driver.implicitly_wait(10)
        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self):
        return Main(self._driver)
