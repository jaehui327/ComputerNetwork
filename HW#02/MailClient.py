import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

mailServer = 'smtp.naver.com'
port = 465

userID = 'jaehui327'
userPW = 'passwd'

FROM = 'jaehui327@naver.com'
TO = 'jaehee0327@inu.ac.kr'

text = '03. Mail Client'
msg = MIMEMultipart()
msg['Subject'] = '[Socket Programming]201601692'
msg['From'] = 'jaehui327@naver.com'
msg['To'] = 'jaehee0327@inu.ac.kr'
msg.attach(MIMEText(text, 'plain', 'utf-8'))

smtp = smtplib.SMTP_SSL(mailServer, port)
smtp.login(userID, userPW)
smtp.sendmail(FROM, TO, msg.as_string())

smtp.quit()

print("completed")
