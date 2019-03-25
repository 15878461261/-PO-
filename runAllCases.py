import unittest,os,time,sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from HTMLTestRunner import HTMLTestRunner
def allTest():
    ''''获取testCases下面的所有测试用例'''
    case = os.path.join(os.path.dirname(__file__),'testCases')
    suite = unittest.defaultTestLoader.discover(case,pattern='test*.py')
    return  suite
#print(allTest())


def getTime():
    '''获取系统当前时间'''
    return time.strftime("%Y_%m_%d %H_%M_%S")
def run():
    report = os.path.join(os.path.dirname(__file__),'report',getTime()) + '_report.html'
    HTMLTestRunner(stream=open(report,'wb'),title='po自动化测试设计模式',description='window8 chrom67').run(allTest())

if __name__ == '__main__':
    run()