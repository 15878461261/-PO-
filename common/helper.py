import logging,os
import xlrd
class Helper(object):
    def readExcles(self,rowx):

        '''
           rowx是行数
           :param rowx:
           :return: 返回的每一行的行数
           '''
        book = xlrd.open_workbook(r'C:\Users\dandan\PycharmProjects\Project\PO\data\xlsx.xls', 'r')
        table = book.sheet_by_index(0)
        return table.row_values(rowx)

    def readusername(self,rowx):
        '''
            rowx返回的是第几行的用户名
            :param rowx:
            :return:
            '''
        return str(self.readExcles(rowx)[0])

    def readpassword(self,rowx):
        '''
               rowx返回的是第几行的密码
               :param rowx:
               :return:
               '''
        return self.readExcles(rowx)[1]

    def exceptText(self,rowx):
       '''
                rowx返回的是第几行的预期结果
                :param rowx:
                :return:
                '''
       return self.readExcles(rowx)[2]

    def dirname(self,filename,filepath = 'data'):
        ''''
        :param filename:文件名
        :param filepath:文件路径
        :return:
        '''
        return os.path.join(os.path.dirname(os.path.dirname(__file__)),filepath,filename)
#per = Helper()
#print(per.dirname('log.md'))


    def log(self,log_content):
        '''定义log日志级别'''
        #定义文件
        logFile = logging.FileHandler(self.dirname('log.md','log'),'a',encoding='utf-8')
        #log格式
        fmt = logging.Formatter(fmt='%(asctime)s-%(name)s-%(levelname)s-%(module)s:%(message)s')
        logFile.setFormatter(fmt)
        #定义日志
        logger1=logging.Logger('logTest',level=logging.DEBUG)
        logger1.addHandler(logFile)
        logger1.info(log_content)
        logFile.close()
