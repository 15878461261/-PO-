import yagmail
#链接邮箱服务器
yag = yagmail.SMTP(user="1393707367@qq.com",password="whvdpysfxoimbabe",host='smtp.qq.com')
#邮箱正文
contents=['jjguughh24556544']
#发送邮件
#yag.send('1393707367@qq.com','Yagmail邮件发送',contents)

#多个接受着发送邮件
#yag.send(['1393707367@qq.com','272500809@qq.com','15878461261@163.com'],'Yagmail邮件发送',contents)

yag.send(['1393707367@qq.com','15878461261@163.com'],'Yagmail邮件发送附件',contents,['fujian.htlm'])