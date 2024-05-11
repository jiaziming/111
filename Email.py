#!/usr/bin/python


#import smtplib
#from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header



mail_host = ''
mail_port = ''

sender_email = ''
receiver_email = ''

mail_username = ''
mail_password = ''

def port_mail(title,context):
    # 构造文本对象，三个参数：文本内容，设置文本格式,设置编码

    massage = MIMEText(context,'plain','utf-8')
    #文本内容 添加 发送者
    massage["FROM"] = sender_email
    #添加接收者
    massage["TO"] = receiver_email
    #文本内容 添加标题
    massage["SUBJECT"] = Header(title,'utf-8')

    # 创建 SMTP 对象，连接目标服务器
    smtpObj = smtplib.SMTP_SSL(mail_host, mail_port)
    # 自己账号登录
    smtpObj.login(mail_user, mail_pass)
    # 发送邮件到目标地址  注意：信息由MTMEText对象 转为 字符串对象
    smtpObj.sendmail(sender_email, receiver_email, massage.as_string())
    # 结束 SMTP 对象
    smtpObj.quit()


if __name__ == '__main__':
    port_mail("至老妖怪的邮件", "老Amy，哪里逃！")


