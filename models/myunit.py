import unittest
from time import sleep
from .public import browser
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from objPage.loginPage import login  # noqa: E402


class myTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):  # 一个测试类(文件)执行打开一次浏览器, 节约每个用例打开一次浏览器的时间
        cls.drv = browser()
        cls.drv.maximize_window()
        cls.drv.implicitly_wait(10)

    def setUp(self):
        self.login = login(self.drv)
        self.login.open()

    def tearDown(self):
        self.drv.refresh()

    @classmethod
    def tearDownClass(cls):
        sleep(3)
        cls.drv.quit()
