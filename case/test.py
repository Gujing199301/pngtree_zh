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

        # 点击导航登录按钮
        self.driver.find_element_by_xpath('//*[@id="v2-head"]/div/div[1]/div[4]/a[1]').click()
        sleep(3)

    # facebook登录
    def test_zh_facebook(self):
        # 点击facebook登录
        self.driver.find_element_by_xpath('//*[@id="base-public-login"]/div[2]/div/div/div/div[1]/div/a[1]').click()
        sleep(3)

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


    def teardown_class(self):

        sleep(2)
        # self.driver.quit()

if __name__ == "__main__":
    pytest.main(['-s','-q','test.py'])


