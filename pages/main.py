import pytest
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
from API_UI_TestFramework.pages.base_page import BasePage


class Main(BasePage):
    def goto_message(self):
        pass

    def goto_workbench(self):
        pass

    def goto_addresslist(self):
        from API_UI_TestFramework.pages.addresslist_page import AddressList
        self._driver.wait_activity(".launch.WwMainActivity", 10)
        # 查找APP首页中的“通讯录”按钮
        el_button_address_list = self._driver.find_element(By.XPATH, '//*[@resource-id="com.tencent.wework:id/f3a" and @text="通讯录"]')
        # 点击通讯录按钮
        el_button_address_list.click()
        return AddressList(self._driver)

    def goto_profile(self):
        pass