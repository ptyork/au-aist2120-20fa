import json
import requests as req
from pprint import pprint as pp
import sys

with open('\\apikeys.json') as fi:
    apikeys = json.loads(fi.read())

key = apikeys["OpenWeather"]

zip = "30904"
if len(sys.argv) > 1:
    zip = sys.argv[1]

resp = req.get(
    "http://api.openweathermap.org/data/2.5/weather",
    params={
        "appid": key,
        "zip": zip,
        "units": 'imperial'
    }
)
# print(resp.text)

data = json.loads(resp.text)

if data["cod"] != 200:
    print("NOT FOUND")
    exit()

# pp(data)

name = data["name"]
temp = data["main"]["temp"]
weather = data["weather"][0]["description"]

print(f"{name} has {weather} and it is {temp}F degrees")

