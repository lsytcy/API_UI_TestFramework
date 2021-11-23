import appium
from appium import webdriver
from selenium import *
from selenium.webdriver.common.by import By

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
# 定位到首页-搜索框
find_searchBar = driver.find_element(By.ID, "com.hd.smarttour:id/searchBar")
# 等待搜索页面展示

find_searchBar.click()
# find_searchBar = driver.find_element(By.ID)
driver.quit()


