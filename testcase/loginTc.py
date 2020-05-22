import unittest
import ddt
import yaml
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from models import myunit, public  # noqa: E402
from config import globalparameter as gl  # noqa: E402
from objPage.loginPage import login  # noqa: E402

f = open(gl.testdata_path + '/' + 'logindata.yaml', encoding='utf-8')
tData = yaml.load(f, Loader=yaml.FullLoader)


@ddt.ddt
class loginTest(myunit.myTest):
    # 登录测试
    def user_login_verf(self, acct='', pwd=''):
        login(self.drv).user_login(acct, pwd)

    @ddt.data(*tData)
    def test_login(self, datayaml):
        self.user_login_verf(datayaml['data']['account'], datayaml['data']['password'])
        po = login(self.drv)
        if datayaml['screenshot'] == 'acct_and_pwd_are_correct':
            self.assertEqual(po.login_success(), datayaml['check'][0])
            public.isrt_img(self.drv, datayaml['screenshot'])
        elif datayaml['screenshot'] == 'acct_empty':
            self.assertEqual(po.acct_in_empty_hint(), datayaml['check'][0])
            public.isrt_img(self.drv, datayaml['screenshot'])
        else:
            self.assertEqual(po.acct_or_pwd_err_hint(), datayaml['check'][0])
            public.isrt_img(self.drv, datayaml['screenshot'])


if __name__ == '__main__':
    unittest.main()
