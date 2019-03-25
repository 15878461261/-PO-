#-*- coding=utf-8 -*-
from selenium.webdriver.support.wait import WebDriverWait  #显示等待
from selenium.webdriver.support import expected_conditions as EC  #判断元素是否被定位


#页面的基础类
class HomePage():
    #构建方法
    def __init__(self,url,dr):
        self.url = url
        self.dr = dr

    #封装元素定位方式
    def find_element(self,*loc):
        try:
            #入参本身就是元祖 不需要加*
            WebDriverWait(self.dr,20).until(EC.visibility_of_element_located(loc))
            return  self.dr.find_element(*loc)
        except:
            print(*loc  + '元素定位在页面中无法找到')




