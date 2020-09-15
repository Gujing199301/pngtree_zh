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

        url = "https://zh.pngtree.com/"
        # 谷歌浏览器打开测试权限
        self.driver.get(url)

        # 浏览器窗口最大化
        self.driver.maximize_window()
        sleep(3)

    # facebook登录
    def test_zh_facebook(self):
        # 点击导航登录按钮
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[6]/div[2]/div/div[2]/div[1]/div[2]/a[2]').click()
        sleep(2)


    def teardown_class(self):

        sleep(2)
        self.driver.quit()

if __name__ == "__main__":
    pytest.main(['-s','-q','test.py'])


