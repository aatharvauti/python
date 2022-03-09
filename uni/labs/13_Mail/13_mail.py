#!/usr/bin/python
from dotenv import load_dotenv
import os
import smtplib
from email.message import EmailMessage

load_dotenv()
# VENV Importing
EMAIL_ADDR = os.getenv('EMAIL_ADDR')
EMAIL_PASS = os.getenv('EMAIL_PASS')
EMAIL_REC1 = os.getenv('EMAIL_REC1')
EMAIL_REC2 = os.getenv('EMAIL_REC2')

contacts = [EMAIL_REC1, EMAIL_REC2]
msg = EmailMessage()
msg['Subject'] = 'Hello from Python'
msg['From'] = EMAIL_ADDR
msg['To'] = contacts
msg.set_content('This message was sent using Python3!')

# with open('output.txt', 'rb') as f: # rb means read bytes mode
#     file_data_main = f.read()
#     file_name_main = f.name
#
# msg.add_attachment(file_data_main, maintype='text', subtype='plain', filename=file_name_main)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:  # prod
    smtp.login(EMAIL_ADDR, EMAIL_PASS)
    smtp.send_message(msg)
    smtp.close()
