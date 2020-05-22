import unittest
from models import public
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from models.public import test_report  # noqa: E402
from config.globalparameter import testcase_path, testreport_path  # noqa: E402


if __name__ == '__main__':
    runner, fp, filename = test_report()
    discover = unittest.defaultTestLoader.discover(start_dir=testcase_path, pattern='*Tc.py')  # 执行以Tc结尾的测试用例文件
    runner.run(discover)
    fp.close()  # 关闭生成的报告
    file_path = public.new_report(testreport_path)  # 查找新生成的报告
    public.send_mail(file_path)  # 调用发邮件模块
