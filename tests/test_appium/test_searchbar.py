import pytest
import time
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
from faker import Faker
import random
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class TestAddContact(object):

    def setup_class(self):
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
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)
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

    # @pytest.mark.parametrize('searchkey,', [
    #     ('酒店'),
    #     ('世界'),
    # ])
    @pytest.mark.skip
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

    @pytest.mark.skip
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

    def test_addcontact(self):
        username = "用户名" + str(random.randint(100, 9999))
        phonenum = int("136" + str(random.randint(10000000, 99999999)))
        # 等待首页加载完成
        self.driver.wait_activity(".launch.WwMainActivity",10)
        # 查找APP首页中的“通讯录”按钮
        el_button_address_list = self.driver.find_element(By.XPATH, '//*[@resource-id="com.tencent.wework:id/f3a" and @text="通讯录"]')
        # 点击通讯录按钮
        el_button_address_list.click()
        self.driver.implicitly_wait(10)
        # 查找到“添加成员”按钮
        el_button_add_member = self.driver.find_element(By.XPATH, '//android.widget.TextView[@text="添加成员"]')
        # 点击“添加成员”
        el_button_add_member.click()
        # 等待添加成员页面出现
        self.driver.wait_activity('.friends.controller.MemberInviteMenuActivity', 10)
        # 定位到“手动输入添加”，并点击
        el_button_manual_input = self.driver.find_element(By.ID, 'com.tencent.wework:id/d8_')
        el_button_manual_input.click()
        # 等待手动添加成员页面
        self.driver.wait_activity(".contact.controller.ContactAddFastModeActivity", 10)
        # 在姓名和手机栏，输入名字和手机号
        el_button_name_input = self.driver.find_element(By.ID, "com.tencent.wework:id/bf7")
        el_button_name_input.send_keys(username)
        el_button_phonenum_input = self.driver.find_element(By.ID, "com.tencent.wework:id/gge")
        el_button_phonenum_input.send_keys(phonenum)
        time.sleep(1)

        # 取消保存后发送邀请通知
        el_button_push = self.driver.find_element(By.ID, "com.tencent.wework:id/g3f")
        el_button_push.click()

        # 点击保存按钮
        el_button_save_contact = self.driver.find_element(By.ID, "com.tencent.wework:id/am4")
        el_button_save_contact.click()
        # toast_text = self.driver.find_element(By.XPATH, "//*[@class='android.widget.Toast']").text
        toast_text = self.driver.find_element(By.XPATH, "//*[contains(@text,'添加成功')]").text
        print(toast_text)
        # time.sleep(1)

        # 获取保存后的toast文案
        # 返回上一级页面
        self.driver.back()

        # 等待返回到Tester页面
        WebDriverWait(self.driver, 10, 0.5).until(ec.presence_of_element_located((By.ID, 'com.tencent.wework:id/j2o')))

        # 断言 保存的用户信息在列表页
        reslut_xpath = '//android.widget.TextView[@text="{}"]'.format(username)
        print(reslut_xpath)
        el_button_new_member = self.driver.find_element(By.XPATH, reslut_xpath)
        print(el_button_new_member.text)
        assert username in el_button_new_member.text





