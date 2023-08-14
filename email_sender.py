#go over to our gmail account and set up 2 factor authentication
#generate app password - 
#create a function to send the mail

from email.message import EmailMessage
from app2 import password #it stores the app password, no need to put .py as it is a python file
import ssl
import smtplib

email_sender = "bhargavi.gunupudi@gmail.com"
email_password = password #safer to create an environment variable and store a password

email_receiver = 'leham93770@vreaa.com'

subject = "My message to you."
#write whatever you want here
body = """                  
When you wake up every morning, wake up with a smile on your face. Ending it all is not the right answer.
You have so much to look forward to as a person. The past will never dictate your future.
"""

#create an instance of the email package library
em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

#we need to create context, we need to import ssl and smt libraries

context = ssl.create_default_context()

#used smtp library to actually send the email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())#converting em details to string
