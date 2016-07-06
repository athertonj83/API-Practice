#sending e-mails
import smtplib

#Bringing in my personal gmail info
with open("C:/Users/Jen/Documents/Python for Windows/gmail_auth.py") as f:
    code = compile(f.read(), "C:/Users/Jen/Documents/Python for Windows/gmail_auth.py" , 'exec')
    exec(code)

email = email_auth.email
pword = email_auth.pword
to_email = email_auth.email

to_james="jim.seconde@googlemail.com"

#1 http://naelshiab.com/tutorial-send-email-python/
msg="This is the message"
#james_msg="I'm sending this using Python! x"

server = smtplib.SMTP('smtp.gmail.com', 587)
print("Y")
server.starttls()
print("X")
server.login(email,pword)
print("C")
server.sendmail(email,to_email,msg)
#server.sendmail(email,to_james,james_msg)
server.quit()
