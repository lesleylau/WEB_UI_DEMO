from .base import page
from time import sleep
from selenium.webdriver.common.by import By
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from config import globalparameter as gl  # noqa: E402
from models.public import getYaml  # noqa: E402

eleData = getYaml(gl.ele_path + '/' + 'login.yaml')


class login(page):
    # 登录页面
    url = '/login'

    acctEle = (By.CSS_SELECTOR, eleData.get_ele(0))
    pwdEle = (By.CSS_SELECTOR, eleData.get_ele(1))
    loginBtnEle = (By.CSS_SELECTOR, eleData.get_ele(2))
    acctEmptyMsg = (By.XPATH, eleData.get_check_ele(0))
    pwdEmptyMsg = (By.XPATH, eleData.get_check_ele(1))
    failMsg = (By.CSS_SELECTOR, eleData.get_check_ele(2))
    successMsg = (By.CSS_SELECTOR, eleData.get_check_ele(3))

    # Action
    def login_acct(self, acct):
        self.find_element(*self.acctEle).send_keys(acct)

    def login_pwd(self, pwd):
        self.find_element(*self.pwdEle).send_keys(pwd)

    def login_btn(self):
        self.find_element(*self.loginBtnEle).click()

    # 定义登录入口
    def user_login(self, acct='admin', pwd='123456'):
        self.open()
        self.login_acct(acct)
        self.login_pwd(pwd)
        self.login_btn()
        sleep(1)

    # 帐户输入为空错误提示
    def acct_in_empty_hint(self):
        return self.find_element(*self.acctEmptyMsg).text

    # 密码输入为空错误提示
    def pwd_in_empty_hint(self):
        return self.find_element(*self.pwdEmptyMsg).text

    # 帐户或密码错误提示
    def acct_or_pwd_err_hint(self):
        return self.find_element(*self.failMsg).text

    # 登录成功提示
    def login_success(self):
        return self.find_element(*self.successMsg).text
