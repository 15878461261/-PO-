#coding=utf-8

import smtplib,uuid
from email.mime.text import MIMEText #邮件模板类


#发邮件相关参数

smtpsever = 'smtp.qq.com'
sender = '1393707367@qq.com'
psw = "whvdpysfxoimbabe"   #邮箱授权码
receiver = '1393707367@qq.com'
port =465

#编辑邮件内容
subject = u"你猜这是啥?"
body = str(uuid.uuid4())
msg = MIMEText(body,'html','utf-8')
msg['from']='1393707367@qq.com'
msg['to']='1393707367@qq.com'
msg['subject']=subject

#链接服务器发送
try:
    smtp=smtplib.SMTP_SSL(smtpsever,port)
    smtp.login(sender,psw)                             #登录
    smtp.sendmail(sender,receiver,msg.as_string())     #发送
    print('邮件发送成功!')
    smtp.quit()
except smtplib.SMTPException as meg:
    print('邮件发送失败！失败原因:{}'.format(meg))