import time
import pytest
from appium import webdriver
from selenium.webdriver.common.by import By

# '''
# # 获取时间戳并输出格式化日期
# now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
#
# print("./screenshot/" + now + "-" +"search.png")
# 链接设备的属性
desired_caps = {
  "platformName": "android",
  "platformVersion": "11.0",
  "deviceName": "72973146",
  "appPackage": "com.hd.smarttour",
  "appActivity": ".activity.SplashActivity",
  "noReset": True
}
# 创建driver，用于操作设备与应用
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
driver.wait_activity(".activity.MainActivity", 10)
# 定位到首页-搜索框
find_searchBar = driver.find_element(By.ID, "com.hd.smarttour:id/searchBar")
# 点击搜索框
find_searchBar.click()
# 等待搜索页面展示
driver.wait_activity(".search.SearchActivity", 10)
# 输入搜索内容“酒店”
searchContentInput = driver.find_element(By.ID, "com.hd.smarttour:id/et_search")
searchContentInput.send_keys("酒店")
driver.get_screenshot_as_file("./screenshot/" + now + "-" +"search.png")
driver.quit()


