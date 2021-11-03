import schedule
import json
import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

def hello():
    print("Hello")

load_dotenv("TOKENS.env")
# Twilio-related keys
account_sid= os.getenv('twilio_account_sid')
auth_token= os.getenv('twilio_auth_token')
twilio_number = os.getenv('twilio_number')
number = os.getenv('number')


client = Client(account_sid, auth_token)

def sendText():
    client.messages.create(
        to = f"+1{number}",
        from_= f"+1{twilio_number}",
        body = "This is a test text the schedule library"
)

sendText()

# # schedule.every(5).seconds.do(hello)
schedule.every(20).seconds.do(sendText)


while True:
    schedule.run_pending()
