import json
import requests as req
from pprint import pprint as pp
import sys

# print(sys.argv)
# exit()

if len(sys.argv) != 2:
    print("YOU DON'T DESERVE THE WEATHER")
    exit()

zip = sys.argv[1]

with open('\\apikeys.json') as fi:
    apikeys = json.loads(fi.read())

key = apikeys["OpenWeather"]

resp = req.get(
    "http://api.openweathermap.org/data/2.5/weather",
    params={
        "appid": key,
        "zip": zip,
        "units": "imperial"
    }
)
# print(resp.text)

weather = json.loads(resp.text)

# pp(weather)

if weather["cod"] != 200:
    print("ERROR FROM WEB")
    exit()

city = weather['name']
cond = weather['weather'][0]['description']
temp = weather['main']['temp']
print(f"The weather in {city} is {cond} and the temp is {temp}F")
