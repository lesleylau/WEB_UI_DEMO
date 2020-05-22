import os

# 获取项目路径
project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]), '.'))

driver_path = project_path + "\\drivers\\chromedriver.exe"

# 元素数据路径
ele_path = project_path + "\\elementinfo\\"

# 测试数据路径
testdata_path = project_path + "\\testdata\\"

# 测试用例路径
testcase_path = project_path + "\\testcase"

# 测试用例执行截图路径
testcase_img_path = project_path + "\\testreport\\img\\"

# 测试报告路径
testreport_path = project_path + "\\testreport\\html\\"

# 设置发送测试报告的公共邮箱、用户名和密码
smtp_sever = 'smtp.qq.com'
smtp_port = '465'
email_sender = "2900577398@qq.com"
email_psw = "zzypkaowgajnddbf"
email_receiver = ["asdvadfgwbw@163.com", "2900577398@qq.com"]
email_subject = "WEB_UI_DEMO_Test_Report"

# 后台管理系统URL访问路径
URL_base = 'http://admin.xttag.cn/#'
