from time import sleep
# noinspection PyUnresolvedReferences
import pytest
from selenium import webdriver
# noinspection PyUnresolvedReferences
import allure

class TestLogin:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        url = "https://pngtree.com/"
        self.driver.get(url)
        sleep(2)
        self.driver.maximize_window()
        sleep(2)

    def test_001(self):
        print('000001')

    def teardown_class(self):
        self.driver.quit()


if __name__ == "__main__":
    pytest.main(['-s','-q','test.py'])






