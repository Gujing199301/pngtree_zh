
# 导包
import time
from time import sleep
from selenium import webdriver
# noinspection PyUnresolvedReferences
import pytest
import unittest
from selenium.webdriver.common.action_chains import ActionChains
# noinspection PyUnresolvedReferences
import allure


class TestZhLogin(unittest.TestCase):

    # 初始化操作
    def setUp(self):
        # # 创建浏览器对象C:\Users\Administrator\AppData\Local\Programs\Python\Python38-32\chromedriver.exe
        # option = webdriver.ChromeOptions()
        #
        # option.binary_location = r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe'

        self.driver = webdriver.Chrome()

        # 英语测试权限
        url = "https://zh.pngtree.com/"

        # 谷歌浏览器打开测试权限
        self.driver.get(url)

        # 浏览器窗口最大化
        self.driver.maximize_window()

        # 无论第一打开页面有没有pv验证都刷新一次页面
        self.driver.refresh()

        # 新窗口打开测试权限，连续刷5次刷新pv
        js = 'window.open("https://pngtree.com/test?pass=zxcvb")'

        self.driver.execute_script(js)

        sleep(1)

        # 切换至新窗口
        f = self.driver.window_handles
        self.driver.switch_to.window(f[1])
        sleep(2)

        i = 0

        for i in range(1):
            self.driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td[1]/table/tbody/tr[3]/td[2]/a').click()

            sleep(3)
            i = i + 1

        self.driver.find_element_by_xpath('//*[@id="TestCompare"]/tbody/tr[3]/td[2]/a').click()
        sleep(2)

        # 关闭当前窗口
        self.driver.close()

        # 切换至原来窗口
        f = self.driver.window_handles

        self.driver.switch_to.window(f[0])
        sleep(2)

        # 设置隐式等待时间
        self.driver.implicitly_wait(10)

        # 点击导航登录按钮
        self.driver.find_element_by_xpath('//*[@id="v2-head"]/div/div[1]/div[4]/a[1]').click()

        sleep(1)

    def test_01(self):
        print("0000001")


    def tearDown(self):

        sleep(2)
        self.driver.quit()



