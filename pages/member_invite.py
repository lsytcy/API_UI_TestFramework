import pytest
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
from API_UI_TestFramework.pages.base_page import BasePage


class MemberInvite(BasePage):
    def addmember_by_manual(self):
        from API_UI_TestFramework.pages.contact_add import ContactAdd
        # 等待添加成员页面出现
        self._driver.wait_activity('.friends.controller.MemberInviteMenuActivity', 10)
        # 定位到“手动输入添加”，并点击
        el_button_manual_input = self._driver.find_element(By.ID, 'com.tencent.wework:id/d8_')
        el_button_manual_input.click()
        return ContactAdd(self._driver)

    def get_toast(self):
        toast_text = self._driver.find_element(By.XPATH, "//*[@class='android.Widget.Toast']").text
        # toast_text = self._driver.find_element(By.XPATH, "//*[contains(@text,'添加成功')]").text
        print(toast_text)
        return toast_text
