from requests.models import Response
import schedule
import json
import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv
load_dotenv("TOKENS.env")

# Api-related variables
account_sid= os.getenv('twilio_account_sid')
auth_token= os.getenv('twilio_auth_token')
twilio_number = os.getenv('twilio_number')
number = os.getenv('number')
openweather_key = os.getenv('openweather_api_key')

# openweather-related variables
city = "lenexa"
state = "us-ks"
units = "imperial"
def get_weather():
    openweather_url= f"http://api.openweathermap.org/data/2.5/weather?q={city},{state}&units={units}&appid={openweather_key}"
    # make a request using the get method from the url
    response = requests.get(openweather_url)
    # json is a file format that allows for data exchange
    weather_data = response.json()
    # extracting/assigning specific data
    temp_cur = weather_data["main"]["temp"]
    temp_min = weather_data["main"]["temp_min"]
    temp_max = weather_data["main"]["temp_max"]
    cur_cond = weather_data["weather"][0]["description"]
    return temp_cur, temp_min, temp_max, cur_cond


client = Client(account_sid, auth_token)
def sendText():
    temp_cur, temp_min, temp_max, cur_cond = get_weather()
    client.messages.create(
        to = f"+1{number}",
        from_= f"+1{twilio_number}",
        body = ("\n"
                "Lenexa\n"
                f"Current temp: {temp_cur}\n"
                f"Min temp: {temp_min}\n"
                f"Max temp: {temp_max}\n"
                f"Condition: {cur_cond}\n"))

schedule.every().day.at("08:00").do(sendText)
schedule.every().day.at("12:00").do(sendText)
schedule.every().day.at("16:00").do(sendText)


while True:
    schedule.run_pending()