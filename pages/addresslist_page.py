from API_UI_TestFramework.pages.member_invite import MemberInvite
from API_UI_TestFramework.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AddressList(BasePage):
    def add_member(self):
        # 查找到“添加成员”按钮
        el_button_add_member = self._driver.find_element(By.XPATH, '//android.widget.TextView[@text="添加成员"]')
        # 点击“添加成员”
        el_button_add_member.click()
        return MemberInvite(self._driver)
