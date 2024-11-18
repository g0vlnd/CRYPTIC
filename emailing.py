import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import time
import os

# def send_email(subject, body, sender, recipients, password, path_image1,path_image2,path_image3,path_image4):
def send_email(subject, body, sender, recipients, password, path_image1,path_image2):

    msg = MIMEMultipart()
    text = MIMEText(body)
    msg.attach(text)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with open (path_image1,'rb') as fp:
        img = MIMEImage(fp.read())
    msg.attach(img)
    with open (path_image2,'rb') as fp:
        img = MIMEImage(fp.read())
    msg.attach(img)
    # with open (path_image3,'rb') as fp:
    #     img = MIMEImage(fp.read())
    # msg.attach(img)
    # with open (path_image4,'rb') as fp:
    #     img = MIMEImage(fp.read())
    msg.attach(img)
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")

# Email details
day=time.strftime("%D").replace("/","-")
subject = f" PUT SOMETHING"
sender = "test@gmail.com" #UPDATE THIS
recipients = [""] #UPDATE THIS
password=os.environ["keymail"] # WILL BE SOMETHING LIKE # keymail='w f u t l q q s d v b a q a c v f' # you will get this somehow from gmail, make a new email

# Define a body of Email
body = f"""
Here is the body with all the info you want to add

"""
# Send Email
send_email(subject, body, sender, recipients, password)