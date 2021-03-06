"""
Web端UI测试
author:tester_cy
"""
from selenium import webdriver
import unittest
import time
import pytest
import glob

"""
运行Selenium环境准备
1、安装selenium-pip install selenium
2、安装Chrome Driver（并添加到环境变量，Chrome driver地址：http://npm.taobao.org/mirrors/chromedriver）
"""


# 通过 pytest -m "标签名"执行指定的测试用例
class Baidu(unittest.TestCase):

    # 初始化打开浏览器，并打开指定网页
    def setUp(self):
        self.driver = webdriver.Chrome(r'D:\chromedriver_win32\chromedriver.exe')
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.baidu.com"

    def test_baidu_search(self):
        driver = self.driver
        driver.get(self.base_url+"/")
        driver.find_element_by_id('kw').send_keys("中国海南海花岛")
        driver.find_element_by_id('su').click()
        time.sleep(2)
        search_results = driver.find_element_by_xpath('//*[@id="6"]/h3/a/em').get_attribute('innerHTML')
        self.assertEqual('中国海南海花岛' in search_results, True)

    @unittest.skip('Skip')
    def test_baidu_set(self):
        driver = self.driver
        driver.get(self.base_url + '/gaoji/preferences.html')
        m = driver.find_element_by_xpath(".//*[@id='nr']")
        m.find_element_by_xpath("//option[@value='10']").click()

    # 关闭浏览器
    def tearDown(self):
        self.driver.quit()