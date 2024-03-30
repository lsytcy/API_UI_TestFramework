import pytest
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from API_UI_TestFramework.common.common_func import get_sys_version
from API_UI_TestFramework.common.common_func import get_devicesname


class TestCheckWeather(object):

    def setup_class(self):
        # 获取系统版本
        platformVersion = get_sys_version()
        # 获取devicename
        deviceName = get_devicesname()
        # 连接设备并打开应用
        desired_caps = {
            "platformName": "android",
            "platformVersion": '6.0.1',
            "deviceName": '127.0.0.1:7555',
            "appPackage": "hko.MyObservatory_v1_0",
            "appActivity": ".myObservatory_app_SplashScreen",
            "dontStopAppOnReset": False,
            "unicodeKeyBoard": True,
            "resetKeyboard": True,
            "noReset": True,

        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(20)
        print("setup_class")

    def teardown_class(self):
        self.driver.quit()
        print("teardown_class")

    def setup(self):
        print('setup_method')
        pass

    def teardown(self):
        print('teardown_method')
        pass

    def test_check_nineday_forecast(self):
        # 等待主页加载
        self.driver.wait_activity("hko.homepage.Homepage2Activity", 10)
        # 定位到首页左上角菜单栏
        find_menu = self.driver.find_element_by_accessibility_id("转到上一层级")
        # 点击菜单按钮
        find_menu.click()
        # 滑动菜单栏
        window_rect = self.driver.get_window_rect()
        width = window_rect["width"]
        height = window_rect["height"]
        # 上下滑动线路的X坐标
        x1 = int(width / 3)
        # 上下滑动的起点和终点的y坐标
        y_start = int(height * 4 / 5)
        y_end = int(height * 1 / 5)
        print("window is :", self.driver.get_window_rect())
        # 从起始点滑动到终点
        time.sleep(2)
        TouchAction(self.driver).press(x=x1, y=y_start).wait(2000).move_to(x=x1, y=y_end).release().perform()
        time.sleep(2)
        # 截图保存搜索结果
        # self.driver.get_screenshot_as_file("./screenshot/search1.png")
        # 查找并点击9-day Frorecast按钮
        self.driver.find_element(By.XPATH, '//*[@resource-id="hko.MyObservatory_v1_0:id/text" and @text="9-Day Forecast"]').click()
        # 断言
        txt = 'An intense winter monsoon will continue to affect the coast of Guangdong in the next couple of days'
        # 9-day Forecast 页面文案
        assert_content = self.driver.find_element(By.ID, 'hko.MyObservatory_v1_0:id/mainAppSevenDayGenSit').text
        assert txt in assert_content

