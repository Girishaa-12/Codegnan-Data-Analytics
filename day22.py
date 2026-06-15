#Date and time : python provides the built in date and time module to work with dates and time
'''
import datetime
today = datetime.date.today()
now = datetime.datetime.now()
print(now)
print(today)
'''

'''
import datetime
now = datetime.datetime.now()
print(f"year is {now.year}")
print(f"month is {now.month}")
print(f"day is {now.day}")
print(f"hour is {now.hour}")
print(f"minutes is {now.minute}")
print(f"second is {now.second}")
'''

#formatting date and time: strftime() is used to formate date and time
'''
%d - day
%m - month
%y - year
%H - hour
%S - second
%M - minute
'''

'''
import datetime
now = datetime.datetime.now()
print(now.strftime("%d-%m-%y"))
print(now.strftime("%H-%M-%S"))
'''

'''
import datetime
date1= datetime.date(2026,5,12)
date2= datetime.date(2026,6,15)
diff = date2 - date1
print(diff)
'''

#timedelta - is used to work with future date, and also only work with date
'''
import datetime
today = datetime.date.today()
future = today+datetime.timedelta(days = 7)
print(future)
'''

'''
import datetime
day = datetime.date.today()
print(day.weekday())
'''

#ctime - a particuclar day and mnth
'''
import datetime
day = datetime.date.today()
print(day.ctime())
'''
#calendar
'''
import calendar
import datetime
today = datetime.date.today()
year = today.year
month = today.month
print(calendar.month(year,month))
'''
#a particular month
'''
import calendar
year = 2026
month = 5
print(calendar.month(year,month))
'''

#to find full year
'''
import calendar
year = 2004
print(calendar.calendar(year))
'''
#to find leap year
'''
import calendar
year = 2004
print(calendar.isleap(year))
'''

#to send a mail at one praticular time and date

import smtplib
from email.message import EmailMessage
import time
from datetime import datetime

sender_mail = "venkateshgirisha14@gmail.com"
password = "myugchtintuqfjgv"
receiver_mail = "poornima.pappu05@gmail.com"
send_time = "2026-06-15 10:45:00"

while True:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if now >= send_time:
        msg = EmailMessage()
        msg["Subject"] = "Test Mail"
        msg["From"] = sender_mail
        msg["To"] = receiver_mail
        msg.set_content("Hello")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(sender_mail, password)
            smtp.send_message(msg)

        print("Mail Sent Successfully!")
        break

    time.sleep(1)

