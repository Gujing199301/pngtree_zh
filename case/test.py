from time import sleep
# noinspection PyUnresolvedReferences
import pytest
from selenium import webdriver
# noinspection PyUnresolvedReferences
import allure
from selenium.webdriver import ActionChains


class TestLogin:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        url = "https://zh.pngtree.com/"
        self.driver.get(url)
        sleep(2)
        self.driver.maximize_window()
        sleep(2)

        # 点击登录按钮
        self.driver.find_element_by_xpath('//*[@id="v2-head"]/div/div[1]/div[4]/a[1]').click()


    def test_en_facebook(self):
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

        sleep(3)

        # facebook登录窗口自行关闭，切换至原来窗口（登录首页）
        f = self.driver.window_handles

        self.driver.switch_to.window(f[0])

        print('英语facebook登录成功')

        # 刷新页面，可能有优惠券遮罩
        self.driver.refresh()

        sleep(4)

        # 定位用户头像（邮箱登录头像和其他登录方式xpath略有不同）
        user_img = self.driver.find_element_by_xpath(
            '//*[@id="v2-head"]/div/div[1]/div[5]/a[1]/div/img')

        sleep(1)

        # 创建鼠标对象
        action = ActionChains(self.driver)

        action.move_to_element(user_img).perform()
        sleep(3)

        # 点击退出账号
        self.driver.find_element_by_xpath(
            '//*[@id="v2-head"]/div/div[1]/div[5]/div/div[4]/a[5]/i').click()
    def teardown_class(self):
        self.driver.quit()


if __name__ == "__main__":
    pytest.main(['-s','-q','test.py'])






