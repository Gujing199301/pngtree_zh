from time import sleep
# noinspection PyUnresolvedReferences
import pytest
from selenium import webdriver
# noinspection PyUnresolvedReferences
import allure
# noinspection PyUnresolvedReferences
import unittest

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        url = "https://zh.pngtree.com/"
        self.driver.get(url)
        sleep(2)
        self.driver.maximize_window()
        sleep(2)

    def test_001(self):
        print('000001')

    def tearDown(self):

        self.driver.quit()






