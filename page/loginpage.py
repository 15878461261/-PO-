from  selenium.webdriver.common.by import By #定位方法
from time import sleep
from PO.basepage.homepage import HomePage #导入基础类

#登录的页面类

class LoginPage(HomePage):
    # 定位器
    #用户名
    login_loc = (By.XPATH,'/html/body/div[1]/div/span/a[1]')
    username_loc = (By.ID,'mobilePhone')
    password_loc = (By.ID,'password')
    loginBtn_loc = (By.ID,'loginBtn')
    logoutBtn_loc = (By.CSS_SELECTOR,'a.fc-blue.mr-5')
    userNull_loc = (By.CSS_SELECTOR,'#error > span')
    passwordNull_loc = (By.CSS_SELECTOR,'#error > span')

    #打开登录页面
    def openLoginPage(self):
        self.dr.get(self.url)
        self.dr.refresh
        self.dr.maximize_window()
        sleep(2)
    def click_login(self):
         self.find_element(*self.login_loc).click()
        #输入用户名
    def input_userName(self,userName):
        self.find_element(*self.username_loc).send_keys(userName)

    def input_passWord(self,password):
        self.find_element(*self.password_loc).send_keys(password)

    def click_loginBtn(self):
        self.find_element(*self.loginBtn_loc).click()

    def get_asserText(self):
        return self.find_element(*self.logoutBtn_loc).text

    def get_userNullText(self):
        return self.find_element(*self.userNull_loc).text

    def get_passWordNullText(self):
        return self.find_element(*self.passwordNull_loc).text




