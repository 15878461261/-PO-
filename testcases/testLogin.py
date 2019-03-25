from PO.page.loginpage import *
from selenium import webdriver
import unittest,logging
from PO.common.helper import Helper


class TestLogin(unittest.TestCase,Helper):
    def setUp(self):
        self.url = "https://www.gjfax.com/"
        self.dr = webdriver.Chrome()
        self.dr.implicitly_wait(30)
        self.loginpage = LoginPage(self.url,self.dr)

      #正常的登录
    def testlogin(self):
        self.loginpage.openLoginPage()
        self.log('正常的登录，po自动化测试- ->打开登录页面')
        self.loginpage.click_login()
        self.loginpage.input_userName(self.readusername(1))
        self.log('正常的登录，po自动化测试- ->输入账号')
        self.loginpage.input_passWord(self.readpassword(1))
        self.log('正常的登录，po自动化测试- ->输入密码')
        self.loginpage.click_loginBtn()
        self.log('正常的登录，po自动化测试- ->点击登录按钮')
        self.assertEqual(self.loginpage.get_asserText(), self.exceptText(1))
        self.log('正常的登录，po自动化测试- ->验证登录是否成功')

    def test_pass_null(self):
        self.loginpage.openLoginPage()
        self.log('密码为空，po自动化测试- ->打开登录页面')
        self.loginpage.click_login()
        self.loginpage.input_userName(self.readusername(2))
        self.log('密码为空，po自动化测试- ->输入账号')
        self.loginpage.input_passWord(self.readpassword(2))
        self.log('密码为空，po自动化测试- ->输入密码')
        self.loginpage.click_loginBtn()
        self.log('密码为空，po自动化测试- ->点击登录按钮')
        self.assertEqual(self.loginpage.get_passWordNullText(), self.exceptText(2))
        self.log('密码为空，po自动化测试- ->验证提示信息是否正确')

    def test_user_null(self):
        self.loginpage.openLoginPage()
        self.log('账号为空，po自动化测试- ->打开登录页面')
        self.loginpage.click_login()
        self.loginpage.input_userName(self.readusername(3))
        self.log('账号为空，po自动化测试- ->输入账号')
        self.loginpage.input_passWord(self.readpassword(3))
        self.log('账号为空，po自动化测试- ->输入密码')
        self.loginpage.click_loginBtn()
        self.log('账号为空，po自动化测试- ->点击登录按钮')
        self.assertEqual(self.loginpage.get_userNullText(), self.exceptText(3))
        self.log('账号为空，po自动化测试- ->验证提示信息是否正确')


if __name__ == '__main__':
    unittest.main(verbosity=2)

