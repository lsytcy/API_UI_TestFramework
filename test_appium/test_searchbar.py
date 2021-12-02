import pytest
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction


class TestSearchBar(object):

    def setup(self):
        # 连接设备并打开应用
        desired_caps = {
            "platformName": "android",
            "platformVersion": "11.0",
            "deviceName": "72973146",
            "appPackage": "com.hd.smarttour",
            "appActivity": ".activity.SplashActivity",
            "dontStopAppOnReset": False,
            "unicodeKeyBoard": True,
            "resetKeyboard": True,
            "noReset": True,

        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize('searchkey,', [
        ('酒店'),
        ('世界'),
    ])
    def test_search_hotel(self, searchkey):
        self.driver.implicitly_wait(5)
        self.driver.wait_activity(".activity.MainActivity", 10)
        # 定位到首页-搜索框
        find_searchbar = self.driver.find_element(By.ID, "com.hd.smarttour:id/searchBar")
        # 点击搜索框
        find_searchbar.click()
        # 等待搜索页面展示
        self.driver.wait_activity(".search.SearchActivity", 10)
        # 输入搜索内容“酒店”
        searchcontentinput = self.driver.find_element(By.ID, "com.hd.smarttour:id/et_search")
        # 输入搜索关键词“酒店”
        searchcontentinput.send_keys(searchkey)
        # 截图保存搜索结果
        # self.driver.get_screenshot_as_file("./screenshot/search1.png")
        # 定位到别墅酒店，并点击别墅酒店
        find_villahotel = self.driver.find_element(By.XPATH, '//*[@resource-id="com.hd.smarttour:id/searchResult"]//.[@resource-id="com.hd.smarttour:id/title"]')
        result = find_villahotel.text
        print(result)
        assert searchkey in result
        #
        # self.driver.get_screenshot_as_file("./screenshot/search2.png")

    # @pytest.mark.skip
    def test_touchaction(self):
        action = TouchAction(self.driver)
        self.driver.wait_activity(".activity.MainActivity", 10)
        # 获取屏幕的尺寸
        window_rect = self.driver.get_window_rect()
        # 屏幕的宽高
        width = window_rect["width"]
        height = window_rect["height"]
        # 上下滑动线路的X坐标
        x1 = int(width/2)
        # 上下滑动的起点和终点的y坐标
        y_start = int(height * 4/5)
        y_end = int(height * 1/5)
        print("window is :", self.driver.get_window_rect())
        # 从起始点滑动到终点
        action.press(x=x1, y=y_start).wait(2000).move_to(x=x1, y=y_end).release().perform()
