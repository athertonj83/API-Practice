#sending e-mails
import smtplib

#Bringing in my personal gmail info
with open("C:/Users/Jen/Documents/Python for Windows/gmail_auth.py") as f:
    code = compile(f.read(), "C:/Users/Jen/Documents/Python for Windows/gmail_auth.py" , 'exec')
    exec(code)

email = email_auth.get_email
pword = email_auth.get_pword
to_email = email_auth.get_to_email


#2 http://www.tutorialspoint.com/python/python_sending_email.htm
# msg="Hellooooo"
# try:
#    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
#    smtpObj.sendmail(email, to_email, msg)
#    print("Successfully sent email")
# except Exception:
#    print("Error: unable to send email")

#1 http://naelshiab.com/tutorial-send-email-python/
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders



# msg = MIMEMultipart()
# msg['From'] = email
# msg['To'] = to_email
# msg['Subject'] = "JEN'S SUBJECT OF THE MAIL"
# body = "TEXT YOU WANT TO SEND - THIS SHOULD BE IN THE BODY"
# print("A")
# msg.attach(MIMEText(body, 'plain','utf-8'))
# print("B")
# text = msg.as_string()
# print("C")
msg="This is the message"

server = smtplib.SMTP('smtp.gmail.com', 587)
print("Y")
server.starttls()
print("X")
server.login(email,pword)
print("C")
server.sendmail(email,to_email,msg)
server.quit()



# 3 http://stackoverflow.com/questions/6270782/how-to-send-an-email-with-python?rq=1
# from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
# fp = open("Test_for_email.txt",'rb')
# # Create a text/plain message
# msg = MIMEText(fp.read())
# fp.close()
#
# # me == the sender's email address
# # you == the recipient's email address
# msg['Subject'] = 'The contents'
# msg['From'] = email
# msg['To'] = to_email
#
# # Send the message via our own SMTP server, but don't include the
# # envelope header.
# s = smtplib.SMTP('smtp.gmail.com', 587)
# s.sendmail(email, [to_email], msg.as_string())
# s.quit()
