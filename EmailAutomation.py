#SMTP:(simple mail transfer protocol):
'''it helps to communicate with our system
this is used to send emails from server to server to another'''
#note:
#1.SMTP SSL port -465
#2.SMTP TLS Port - 587
'''import smtplib'''

#Email Message class
'''
msg['subject'] = 'SMTP ON Mail'
msg['From'] = 'sender@mail.com'
msg['To'] = 'Receiver@mail.com'
'''
'''import smtplib
from email.message import EmailMessage
sender = 'venkateshgirisha14@gmail.com'
password =  'rbmybdbhmkkjskvk'
a = EmailMessage()
a['subject'] = "welcom mail"
a['From'] = sender 
a['To'] = "aswininarava@gmail.com"
a.set_content("Hello")
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
server.send_message(a)
server.quit()'''

#to send bulk mails
import smtplib
from email.message import EmailMessage
sender = 'venkateshgirisha14@gmail.com'
password =  'vpigctotsfqzzuwx'
receiver = ['girishaaa57@gmail.com','venkateshgirisha4@gmail.com']
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender,password)
for email in receiver:
    a = EmailMessage()
    a['subject'] = "welcome mail"
    a['From'] = sender
    a['To'] = email
    a.set_content("Hello")
    server.send_message(a)
server.quit()

