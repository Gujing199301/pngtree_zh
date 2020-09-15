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

        # 关闭当前窗口
        self.driver.close()

        # 切换至原来窗口
        f = self.driver.window_handles

        self.driver.switch_to.window(f[0])
        sleep(2)

        # 设置隐式等待时间
        self.driver.implicitly_wait(10)

    def setUp(self):

        sleep(1)

        # 点击导航登录按钮
        self.driver.find_element_by_xpath('//*[@id="v2-head"]/div/div[1]/div[4]/a[1]').click()

        sleep(1)

    # email登录
    def test_zh_email(self):

        # 输入用户名:hqt21842@evonb.com
        self.driver.find_element_by_id('base-public-login-email-text').send_keys('1280365716@qq.com ')

        # 输入密码:hqt21842@evonb.com
        self.driver.find_element_by_id('base-public-login-password-text').send_keys('1280365716@qq.com  ')

        # 点击登录
        self.driver.find_element_by_id('base-sub-Login-Btn').click()

        sleep(2)

        print('繁体邮箱登录成功')

        # 刷新页面，可能有优惠券遮罩
        self.driver.refresh()

        sleep(4)

        # 定位用户头像（邮箱登录头像和其他登录方式xpath略有不同）
        user_img = self.driver.find_element_by_xpath('//*[@id="v2-head"]/div/div[1]/div[5]/a[1]/div/img')

        # 创建鼠标对象
        action = ActionChains(self.driver)

        action.move_to_element(user_img).perform()
        sleep(3)

        # 点击退出账号
        self.driver.find_element_by_xpath(
            '//*[@id="v2-head"]/div/div[1]/div[5]/div/div[4]/a[5]/i').click()

    # # google登录
    # def test_zh_google(self):
    #
    #     # 点击谷歌登录
    #     self.driver.find_element_by_xpath('//*[@id="base-public-login"]/div[2]/div/div/div/div[1]/div/a[1]').click()
    #
    #     # 新打开一个窗口（弹窗）,切换至第2个窗口
    #     f = self.driver.window_handles
    #     self.driver.switch_to.window(f[1])
    #
    #     # 窗口最大化
    #     self.driver.maximize_window()
    #
    #     # 填写谷歌账号
    #     self.driver.find_element_by_id('identifierId').send_keys('gujingqwertyuiop@gmail.com')
    #     sleep(1)
    #
    #     # 点击下一步
    #     self.driver.find_element_by_xpath(
    #         '//*[@id="identifierNext"]/span'
    #         ).click()
    #     sleep(3)
    #
    #
    #     # 填写谷歌密码
    #     self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys('gujing199301')
    #     sleep(3)
    #
    #     # 点击下一步
    #     # self.driver.find_element_by_css_selector('#passwordNext > span > span').click()
    #     self.driver.find_element_by_xpath('//*[@id="passwordNext"]/span').click()
    #
    #     sleep(3)
    #
    #     # 谷歌登录窗口自行关闭，切换至原来窗口（登录首页）
    #     f = self.driver.window_handles
    #
    #     self.driver.switch_to.window(f[0])
    #
    #
    #     print('繁体谷歌登录成功')

    #     # 刷新页面，可能有优惠券遮罩
    #     self.driver.refresh()
    #
    #     sleep(3)
    #
    #     # 定位用户头像（邮箱登录头像和其他登录方式xpath略有不同）
    #     user_img=self.driver.find_element_by_xpath('//*[@id="wrapper"]/div[5]/div/div[1]/div[2]/div[5]/a[1]/div/img')
    #
    #     # 创建鼠标对象
    #     action = ActionChains(self.driver)
    #
    #     action.move_to_element(user_img).perform()
    #     sleep(3)
    #
    #     # 点击退出账号
    #     self.driver.find_element_by_xpath(
    #             '//*[@id="wrapper"]/div[4]/div/div[1]/div[2]/div[5]/div/div[4]/a[5]/i').click()

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

    def tearDown(self):

        sleep(1)

        # 刷新页面确认退出
        self.driver.refresh()
        sleep(2)

        try:
            # 定位注册弹窗中的文案
            login = self.driver.find_element_by_xpath('//*[@id="base-register-window"]/div[2]/div[1]/div/div[2]/div[1]/p[1]')
            self.driver.refresh()
            print('触发3次PV，已刷新')
            sleep(2)

        except ArithmeticError:
            # 如有异常说明没有触发3次PV弹注册弹窗，不需要需要刷新页面
            print('未触发3次PV弹注册弹窗')

        finally:
            print('继续执行')

    def teardown_class(self):

        sleep(2)
        self.driver.quit()


