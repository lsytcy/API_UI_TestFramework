from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
import logging


class BasePage:
    # 弹窗处理的黑名单
    logging.basicConfig(level=logging.INFO)
    _black_list = [
        (By.XPATH, "//*[@text='确认']"),
        (By.XPATH, "//*[@text='下次再说']"),
        (By.XPATH, "//*[@text='确定']"),
    ]
    _max_num = 3
    _error_num = 0

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value: str = None):
        logging.info(locator)
        logging.info(value)
        element:WebElement
        try:
            if isinstance(locator, tuple):
                element = self._driver.find_element(*locator)
            else:
                element = self._driver.find_element(locator, value)
            # 找到之前_error_num 归0
            self._error_num = 0
            # 隐式等待回复原来的等待
            self._driver.implicitly_wait(10)
            return element
        except Exception as e:
            # 出现异常， 将隐式等待时间设置短一点为1S
            self._driver.implicitly_wait(1)
            # 判断异常处理次数
            if self._error_num > self._max_num:
                raise e
            self._error_num += 1
            # 处理黑名单里面的弹窗
            for ele in self._black_list:
                elelist = self._driver.find_elements(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    # 处理完弹窗，再去查找目标元素
                    return self.find(locator, value)