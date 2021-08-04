#task1
from urllib import request
import praw

remote_url = 'https://www.google.com/robots.txt'

local_file = 'local_copy.txt'

request.urlretrieve(remote_url, local_file)
#task2

# TASK2

# task3
import requests

api_key = "4256b3de394a56a86ee35e43af6f5c2e"

city = input("Enter city name: ")
data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}")

print(f"Location: {data.json().get('name')}, {data.json().get('sys').get('country')}")
print(f"Temperature: {data.json().get('main')['temp']}°C")
print(f"Weather: {data.json().get('weather')[0].get('main')}")
print(
    f"Min/Max Temperature: {data.json().get('main')['temp_min']}°C/{data.json().get('main')['temp_max']}°C"
)
print(f"Humidity: {data.json().get('main')['humidity']}%")
print(f"Wind: {data.json().get('wind')['speed']} km/h")