# 导包
import time
from time import sleep
from selenium import webdriver
# noinspection PyUnresolvedReferences
import pytest
from selenium.webdriver.common.action_chains import ActionChains


class TestZhLogin:

    # 初始化操作
    def setup_class(self):

        # 创建浏览器对象
        self.driver = webdriver.Chrome()

        # 英语测试权限
        url = "https://www.baidu.com/"

        # 谷歌浏览器打开测试权限
        self.driver.get(url)

        # 浏览器窗口最大化
        self.driver.maximize_window()


    # facebook登录
    def test_zh_facebook(self):
        self.driver.find_element_by_id('kw').send_keys("java")
        self.driver.find_element_by_id('su').click()
        sleep(3)


    def teardown_class(self):

        sleep(2)
        self.driver.quit()


