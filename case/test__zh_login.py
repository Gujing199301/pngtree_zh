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
        # # 静态IP：102.23.1.105：2005
        # # 阿布云动态IP：http://D37EPSERV96VT4W2:CERU56DAEB345HU90@proxy.abuyun.com:9020
        # PROXY = "proxy_host:proxy:port"
        # options = webdriver.ChromeOptions()
        # desired_capabilities = options.to_capabilities()
        # desired_capabilities['proxy'] = {
        #     "httpProxy": PROXY,
        #     "ftpProxy": PROXY,
        #     "sslProxy": PROXY,
        #     "noProxy": None,
        #     "proxyType": "MANUAL",
        #     "class": "org.openqa.selenium.Proxy",
        #     "autodetect": False
        # }
        # self.driver = webdriver.Chrome(desired_capabilities=desired_capabilities)

        # 创建浏览器对象
        self.driver = webdriver.Chrome()

        self.driver.implicitly_wait(10)

        # 繁体首页
        url = "https://zh.pngtree.com/"

        # 谷歌浏览器打开繁体首页
        self.driver.get(url)

        # 浏览器窗口最大化
        self.driver.maximize_window()

        # 无论第一打开页面有没有pv验证都刷新一次页面
        self.driver.refresh()

        # 新窗口打开测试权限
        js = 'window.open("https://pngtree.com/test?pass=zxcvb")'

        self.driver.execute_script(js)

        sleep(2)

        # 切换至新窗口
        f = self.driver.window_handles
        self.driver.switch_to.window(f[1])
        sleep(2)

        # 变成美国ip
        self.driver.find_element_by_xpath('//*[@id="TestCompare"]/tbody/tr[3]/td[2]/a').click()
        sleep(3)

        i = 0
        for i in range(1):
            self.driver.find_element_by_xpath('/html/body/div/table/tbody/tr/td[1]/table/tbody/tr[3]/td[2]/a').click()

            sleep(3)
            i = i + 1
        sleep(1)

        # 关闭当前窗口
        self.driver.close()

        # 切换至原来窗口
        f = self.driver.window_handles

        self.driver.switch_to.window(f[0])
        sleep(2)

        # 点击导航登录按钮
        self.driver.find_element_by_xpath('//*[@id="v2-head"]/div/div[1]/div[4]/a[1]').click()

        sleep(1)

    # facebook登录
    def test_zh_facebook(self):

        # 点击facebook登录
        self.driver.find_element_by_xpath('//*[@id="base-public-login"]/div[2]/div/div/div/div[1]/div/a[1]').click()

        # 新打开一个窗口（弹窗）,切换至第2个窗口
        f = self.driver.window_handles
        self.driver.switch_to.window(f[1])

        # 填写fecebool账号
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys('2505312014@qq.com')
        # 输入facebook密码
        self.driver.find_element_by_xpath('//*[@id="pass"]').send_keys('pngtree2019')

        # 点击登录按钮
        self.driver.find_element_by_xpath('//*[@id="loginbutton"]').click()

        sleep(2)

        # facebook登录窗口自行关闭，切换至原来窗口（登录首页）
        f = self.driver.window_handles

        self.driver.switch_to.window(f[0])

        print('繁体facebook登录成功')

        sleep(3)

        # 多刷新几次页面，繁体有第4次PV弹优惠券
        self.driver.refresh()
        sleep(1)

        self.driver.refresh()
        sleep(1)

        self.driver.refresh()
        sleep(1)

        self.driver.refresh()
        sleep(1)

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

    def tearDown(self):

        sleep(2)
        self.driver.quit()
