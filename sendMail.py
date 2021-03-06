import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
 
import datetime

d = datetime.date.today()
filename = "bookmarks_"+str(d.month)+"_"+str(d.day)+"_"+str(d.year)
filepath = r"C:\Users\username\Documents\bm_export_files\\"+filename

 
fromaddr = "sender's email"
toaddr = "receiver's email"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Latest bookmarks"
 
body = ""
msg.attach(MIMEText(body, 'plain'))

attachment = open(filepath,'rb')

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
 
msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "yourpassword")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()