import pytest
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
import random
from API_UI_TestFramework.pages.base_page import BasePage


class ContactAdd(BasePage):
    username = "用户名" + str(random.randint(100, 9999))
    phonenum = int("136" + str(random.randint(10000000, 99999999)))

    def input_name(self):
        # 输入完成停留在当前页面，所以return self
        el_button_name_input = self._driver.find_element(By.ID, "com.tencent.wework:id/bf7")
        el_button_name_input.send_keys(ContactAdd.username)
        return self

    def input_number(self):
        el_button_phonenum_input = self._driver.find_element(By.ID, "com.tencent.wework:id/gge")
        el_button_phonenum_input.send_keys(ContactAdd.phonenum)
        return self

    def click_save(self):
        from API_UI_TestFramework.pages.member_invite import MemberInvite
        # 取消保存后发送邀请通知
        el_button_push = self._driver.find_element(By.ID, "com.tencent.wework:id/g3f")
        el_button_push.click()

        # 点击保存按钮
        el_button_save_contact = self._driver.find_element(By.ID, "com.tencent.wework:id/am4")
        el_button_save_contact.click()
        time.sleep(1)
        return MemberInvite(self._driver)
