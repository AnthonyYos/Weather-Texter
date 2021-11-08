from requests.models import Response
from datetime import datetime
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
city = os.getenv('city')
state = os.getenv('state')
units = "imperial"
openweather_url= f"http://api.openweathermap.org/data/2.5/weather?q={city},{state}&units={units}&appid={openweather_key}"
temp_unit = u"\N{DEGREE SIGN}F"

def get_current_time():
    # Timestamp for texts
    now = datetime.now()
    current_time = now.strftime("%I:%M %p\n%x")
    return current_time

def get_weather():
    # make a request using the get method from the url
    response = requests.get(openweather_url)
    # json is a file format that allows for data exchange
    weather_data = response.json()
    # extracting/assigning specific data
    city_name = weather_data["name"]
    temp_cur = round(weather_data["main"]["temp"])
    temp_min = round(weather_data["main"]["temp_min"])
    temp_max = round(weather_data["main"]["temp_max"])
    cur_cond = weather_data["weather"][0]["description"]
    return temp_cur, temp_min, temp_max, cur_cond, city_name

client = Client(account_sid, auth_token)
def sendText():
    # weather data
    temp_cur, temp_min, temp_max, cur_cond, city_name = get_weather()
    current_time = get_current_time()
    client.messages.create(
        to = f"+1{number}",
        from_= f"+1{twilio_number}",
        body = (
                f"{city_name}\n"
                f"Current temp: {temp_cur}{temp_unit}\n"
                f"Min temp: {temp_min}{temp_unit}\n"
                f"Max temp: {temp_max}{temp_unit}\n"
                f"Condition: {cur_cond}\n"
                f"Sent @ {current_time}"))

schedule.every().day.at("08:00").do(sendText)
schedule.every().day.at("12:00").do(sendText)
schedule.every().day.at("16:00").do(sendText)


while True:
    schedule.run_pending()