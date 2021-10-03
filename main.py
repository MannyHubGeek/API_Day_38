import requests
from datetime import datetime


# Nutri Variables
APP_ID = "053fafa0"
API_KEY = "3073380c15c6d634f151de27ce16e9a8"
URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
QUERY = input("What did you do today?: ")

tempyesterdaydate = datetime.now()
print(tempyesterdaydate)
yesterdate = datetime.strptime(str(tempyesterdaydate), "%Y-%m-%d")
print(yesterdate)

#Sheety variables
sheetyURL = "https://api.sheety.co"
username = "ohueus@yahoo.com"
sheetName = "workouts"
projectName = "workoutTracking"
maybe_api_key = "1de8d06b63e4afef8b1649ffa7a3ef71"
sheety_endpoint = f"{sheetyURL}/{maybe_api_key}/{projectName}/{sheetName}"

headers = {
    # "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0",
}

exercise_params = {
    "query": QUERY,
    "gender": "male",
    "weight_kg": 96.5,
    "height_cm": "173.64",
    "age": 30,
}
# response = requests.post(URL, data=exercise_params, headers=headers)
# print(response.text)

workout = {
     "workouts": {
     "date": "21/07/2020",
     "time": "15:00:00",
     "exercise": "Running",
     "duration": 22,
     "calories": 130,

    }
}

sheety_response = requests.get(sheety_endpoint)
print(sheety_endpoint)
print(sheety_response.text)

