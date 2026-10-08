import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT = 68.1
HEIGHT = 170
AGE = 26

API_Key = os.environ["API_KEY"]
APP_ID = os.environ["APP_ID"]
SHEET_API_KEY = os.environ["SHEET_API_KEY"]

exercise_endpoint  = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
SHEET_ENDPOINT = os.environ["SHEET_ENDPOINT"]

exercise_text = input("Tell me which exercise you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_Key,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%H:%M:%S")
print(result)

bearer_headers = {
    'Authorization': f"Bearer {SHEET_API_KEY}"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=SHEET_ENDPOINT, json=sheet_inputs, headers=bearer_headers)
    print(sheet_response.text)


