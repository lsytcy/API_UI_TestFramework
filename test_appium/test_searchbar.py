import pytest
import time
from appium import webdriver
from selenium.webdriver.common.by import By


class TestSearchBar():

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
            "noReset": True
        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    def teardown(self):
        self.driver.quit()

    def test_search_hotel(self):
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
        searchcontentinput.send_keys("酒店")
        # 截图保存搜索结果
        self.driver.get_screenshot_as_file("./screenshot/search1.png")
        # 定位到别墅酒店，并点击别墅酒店
        find_villahotel = self.driver.find_element(By.XPATH, '//*[@resource-id="com.hd.smarttour:id/title" and @text="别墅酒店（敬请期待）"]')
        result = find_villahotel.text
        assert "别墅酒店" in result
        #
        # self.driver.get_screenshot_as_file("./screenshot/search2.png")

