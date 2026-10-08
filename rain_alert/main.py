import os

import requests
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ["OWM_API_KEY"]
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
latitude = float(os.environ["RAIN_LATITUDE"])
longitude = float(os.environ["RAIN_LONGITUDE"])

weather_params = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella!",
        to=os.environ["ALERT_RECIPIENT_PHONE"],
        from_=os.environ["TWILIO_SENDER_PHONE"],
    )
    print(message.status)
