import os
import yaml
import time
import smtplib
from selenium import webdriver
# from HTMLTestRunner import HTMLTestRunner  # 最原始测试报告
from HTMLTestRunner.HTMLTestRunnerCN import HTMLTestRunner  # 美化版测试报告
# from HTMLTestRunnerChart import HTMLTestRunner  # 带有树状图、饼图，可查看最近十次的测试报告
from config import globalparameter as gl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# 启动浏览器
def browser():
    drv = webdriver.Chrome(executable_path=gl.driver_path)
    return drv


# 读取yaml
class getYaml:
    def __init__(self, filepath):
        self.path = filepath

    def get_yaml(self):
        '''
        加载yaml文件数据
        :param path: 文件路径
        :return:返回数据
        '''
        f = open(self.path, encoding='utf-8')
        data = yaml.load(f, Loader=yaml.FullLoader)
        f.close()
        return data

    def get_alldata(self):
        """
        读取yaml文件数据
        :return: 返回数据
        """
        data = self.get_yaml()
        return data

    def get_caselen(self):
        """
        testcase字典长度
        :return: 字典长度大小
        """
        data = self.alldata()
        length = len(data['testcase'])
        return length

    def get_checklen(self):
        """
        check字典长度
        :return: 字典长度大小
        """
        data = self.alldata()
        length = len(data['check'])
        return length

    def get_ele(self, i):
        """
        获取testcase项的element_info元素
        :param i: 位置序列号
        :return: 返回element_info元素数据
        """
        data = self.get_alldata()
        return data['testcase'][i]['element_info']

    def get_find_type(self, i):
        """
        获取testcase项的find_type元素数据
        :param i: 位置序列号
        :return: 返回find_type元素数据
        """
        data = self.alldata()
        return data['testcase'][i]['find_type']

    def get_operate_type(self, i):
        """
        获取testcase项的operate_type元素数据
        :param i: 位置序列号
        :return: 返回operate_type元素数据
        """
        data = self.alldata()
        return data['testcase'][i]['operate_type']

    def get_check_ele(self, i):
        """
        获取check项的element_info元素
        :param i: 位置序列号
        :return: 返回element_info元素数据
        """
        data = self.get_alldata()
        return data['check'][i]['element_info']

    def get_check_find_type(self, i):
        """
        获取check项的element_info元素
        :param i: 位置序列号
        :return: 返回find_type元素数据
        """
        data = self.alldata()
        return data['check'][i]['find_type']

    def get_check_operate_type(self, i):
        data = self.alldata()
        return data['check'][i]['operate_type']


# 截图
def isrt_img(drv, file_name):
    drv.get_screenshot_as_file(gl.testcase_img_path + file_name + '.png')


# 用HTMLTestRunner实现的测试报告
def test_report():
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = gl.testreport_path + now + '.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='WEB_UI_DEMO_Test_Report', tester='Lesley', description='测试执行情况')
    return runner, fp, filename


# 查找测试报告目录，找到最新生成的测试报告文件
def new_report(test_report):
    lists = os.listdir(test_report)
    lists.sort(key=lambda fn: os.path.getmtime(test_report + "\\" + fn))
    file_new = os.path.join(test_report, lists[-1])
    return file_new


# 定义发送邮件
def send_mail(file_new):
    # 编辑邮件内容
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEMultipart()
    msg["from"] = gl.email_sender  # 发件人
    msg["to"] = ','.join(gl.email_receiver)  # 收件人
    msg["subject"] = gl.email_subject  # 主题

    # 正文
    body = MIMEText(mail_body, "html", "utf-8")
    msg.attach(body)  # 挂起

    # 附件
    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="WEB_UI_DEMO_Test_Report.html"'  # 定义附件名称
    msg.attach(att)  # 挂起

    # 发送邮件
    smtp = smtplib.SMTP_SSL(gl.smtp_sever, gl.smtp_port)
    smtp.login(gl.email_sender, gl.email_psw)
    smtp.sendmail(gl.email_sender, gl.email_receiver, msg.as_string())  # 发送
    smtp.quit()  # 关闭
    print('Email sent success!')


if __name__ == "__main__":
    drv = webdriver.Chrome()
    drv.maximize_window()
    drv.get('http://baidu.com')
    isrt_img(drv, 'baidu.png')

    file_path = new_report('./testreport/html/')
    send_mail(file_path)
