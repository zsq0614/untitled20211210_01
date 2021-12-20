#coding=utf-8
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

mailhost = 'smtp.exmail.qq.com'
port = 465
mailuser = 'shenqi.zou@bluestonehk.com'
mailpass = '123123QWEqwe'

sender = 'shenqi.zou@bluestonehk.com'
receiver = ['1740920807@qq.com']

message = MIMEText('Python自动化发送邮件测试','plain','utf-8')
message['From'] = Header(mailuser,'utf-8')
message['To'] = Header(receiver[0],'utf-8')

subject = 'python smtp mail test'
message['Subject'] = Header(subject,'utf-8')

counter = 0
while counter < 1000 :
    counter += 1
    print counter
    try:
        smtpObj = smtplib.SMTP_SSL()
        smtpObj.connect(mailhost, port)
        smtpObj.login(mailuser, mailpass)
        smtpObj.sendmail(sender, receiver, message.as_string())
        print ('success')
        smtpObj.quit()

    except smtplib.SMTPException:
        print 'error:无法发送邮件'

    time.sleep(60)






