# 导包
import time
from time import sleep
from selenium import webdriver
# noinspection PyUnresolvedReferences
import pytest
import unittest
from selenium.webdriver.common.action_chains import ActionChains


class TestZhLogin(unittest.TestCase):

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

        # 点击搜索词
        self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[6]/div[2]/div/div[2]/div[1]/div[2]/a[2]').click()
        sleep(5)

        # 点击登录
        self.driver.find_element_by_xpath('//*[@id="v2-head"]/div/div[1]/div[4]/a[1]').click()

    # line登录
    def test_zh_line(self):
        # 点击line登录
        self.driver.find_element_by_xpath('//*[@id="base-public-login"]/div[2]/div/div/div/div[1]/div/a[2]/i').click()
        sleep(1)

        # 新打开一个窗口（弹窗）,切换至第2个窗口
        f = self.driver.window_handles
        self.driver.switch_to.window(f[1])

        # 填写line账号
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div/form/fieldset/div[1]/input').send_keys('1165509917@qq.com')

        # 输入line密码
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div/form/fieldset/div[2]/input').send_keys('gujing199301')

        # 点击登录按钮
        self.driver.find_element_by_xpath('//*[@id="app"]/div/div/div/div[2]/div/form/fieldset/div[3]/button').click()

        sleep(2)

        # line登录窗口自行关闭，切换至原来窗口（登录首页）
        f = self.driver.window_handles

        self.driver.switch_to.window(f[0])

        print('繁体line登录成功')

        # 刷新页面，可能有优惠券遮罩
        self.driver.refresh()

        sleep(3)

        # 定位用户头像（邮箱登录头像和其他登录方式xpath略有不同）
        user_img = self.driver.find_element_by_xpath(
            '//*[@id="v2-head"]/div/div[1]/div[5]/a[1]/div/img')

        # 创建鼠标对象
        action = ActionChains(self.driver)

        action.move_to_element(user_img).perform()
        sleep(3)

        # 点击退出账号
        self.driver.find_element_by_xpath(
            '//*[@id="v2-head"]/div/div[1]/div[5]/div/div[4]/a[5]/i').click()



    def teardown_class(self):

        sleep(2)
        self.driver.quit()


