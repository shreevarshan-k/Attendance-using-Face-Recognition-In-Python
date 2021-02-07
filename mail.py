import smtplib
from tkinter import *
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
from datetime import datetime;
   
fromaddr = "shreevarshan.k.2018.it@rajalakshmi.edu.in"
toaddr = "shreevarshan.k@gmail.com"
msg = MIMEMultipart()    
msg['From'] = fromaddr   
msg['To'] = toaddr 
msg['Subject'] = "Attendance Sheet"
body = "Hi! " + str(datetime.now().date()) +" attendance sheet are attached below"
msg.attach(MIMEText(body, 'plain'))
filename = "E:\Face-Recognition/firebase/attendance_files/attendance"+str(datetime.now().date())+'.xls'
attachment = open("E:\Face-Recognition/firebase/attendance_files/attendance"+str(datetime.now().date())+'.xls') 
p = MIMEBase('application', 'octet-stream') 
p.set_payload(open("E:\Face-Recognition/firebase/attendance_files/attendance"+str(datetime.now().date())+'.xls', "rb").read())  
encoders.encode_base64(p)    
p.add_header('Content-Disposition', "attachment; filename= %s" % filename)  
msg.attach(p) 
s = smtplib.SMTP('smtp.gmail.com', 587) 
s.starttls()
s.login(fromaddr, "Shree@2001") 
text = msg.as_string()
s.sendmail(fromaddr, toaddr, text) 
s.quit()
print("Mail sent successfully")
