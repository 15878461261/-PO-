#coding=utf-8


import smtplib
from email.mime.text import MIMEText  #邮件模板类
from email.mime.multipart import MIMEMultipart  #附件类

#发邮件相关参数
smtpsever='smtp.qq.com'
sender='2393989903@qq.com'
psw="hcygozfxeacqdhhb"   #126邮箱授权码
receiver='luruifengx@126.com'
port=465


with open('readme.txt','rb') as fp:    #读文件
    mail_body=fp.read()

#主 题
msg=MIMEMultipart()
msg["from"] = sender
msg["to"] = receiver
msg["subject"] = u"这个我的主题"

#正 文
body=MIMEText(mail_body,"html","utf-8")
msg.attach(body)
att = MIMEText(mail_body,"base64","utf-8")
att["Content-Type"] = "application/octet-stream"
att["Content-Disposition"] = 'attachment; filename="test_report.html"'
msg.attach(att)

#链接服务器发送
try:
	smtp = smtplib.SMTP_SSL(smtpsever,port)
	smtp.login(sender,psw)                          #登录
	smtp.sendmail(sender,receiver,msg.as_string())  #发送
	print('邮件发送成功！')
	smtp.quit()                                     #关闭
except smtplib.SMTPException as meg:
	print('邮件发送失败！失败原因:{}'.format(meg))











# try:
#     smtp=smtplib.SMTP()
#     smtp.connect(smtpsever)                     #连接服务器
#     smtp.login(sender,psw)
# except:
#     smtp=smtplib.SMTP_SSL(smtpsever,port)
#     smtp.login(sender,psw)  #登录
# smtp.sendmail(sender,receiver,msg.as_string())  #发送
# smtp.quit()
