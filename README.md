# Weather-Texter
Weather texter sends a series of texts of the current temperature, daily high, daily low, and current condtions throughtout the day.

## Requirements
Create an env file "TOKENS" and place it within the weather-texter directory.<br>
Get your own keys from openweather and twilio.<br>
Below is the content for your env file.
* openweather_api_key = Your Openweather API Key<br>
* twilio_account_sid = Your Twilio SID<br>
* twilio_auth_token = Your Twilio Token<br>
* twilio_number = Sender Phone Number (e.g.: 1234567890)<br>
* number = Receiver Phone Number (e.g: 0987654321)<br>

## Variables You Need to Fill
```python
# Fill out each string to match your specific needs.
city = "city name"
state = "us-state abbreviation" # Or country abbreviation if not in the US (e.g: uk)
units = "system unit" # imperial, metric, or standard

# If the imperial system isn't being used replace fahrenheit symbol (F) with celcius or kelvin
temp_unit = u"\N{DEGREE SIGN}F"

# Refer to https://openweathermap.org/current#data for any additional changes you want to make to the request url.
openweather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{state}&units={units}&appid={openweather_key}"

# If these times don't suit your needs, refer to the schedule library to make changes for your specific needs
schedule.every().day.at("08:00").do(sendText)
schedule.every().day.at("12:00").do(sendText)
schedule.every().day.at("16:00").do(sendText)
