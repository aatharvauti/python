import dotenv
import sys
import os
from dotenv import load_dotenv
from twilio.rest import Client

# Credentials
load_dotenv()

TWILIO_SID = os.getenv('TWILIO_SID')
TWILIO_AUTH = os.getenv('TWILIO_AUTH')
TWILIO_NUMBER = os.getenv('TWILIO_NUMBER')

client = Client(
    TWILIO_SID, 
    TWILIO_AUTH
)

for msg in client.messages.list():
   print(msg.body)

msg = client.messages.create(
    # to="<mobile number with country code>",
    from_=TWILIO_NUMBER,
    body="Hello from Python 🚀",
)

print(f"Created a new message: {msg.sid}")

client.run(os.getenv('TWILIO_SID'))
client.run(os.getenv('TWILIO_AUTH'))
client.run(os.getenv('TWILIO_NUMBER'))
