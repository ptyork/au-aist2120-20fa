import json
import requests as req
from pprint import pprint as pp
import sys

with open('\\apikeys.json') as fi:
    apikeys = json.loads(fi.read())

# print(apikeys.keys())
key = apikeys["OpenWeather"]

zip = "30904"

if len(sys.argv) > 1:
    zip = sys.argv[1]

resp = req.get(
    "http://api.openweathermap.org/data/2.5/weather",
    # "http://api.openweathermap.org/data/2.5/forecast",
    params={
        "appid": key,
        "zip": zip,
        "units": "imperial"
    }
)
# print(resp.text)
data = json.loads(resp.text)
# pp(data)

print(f"The Current Temp in {data['name']} is {data['main']['temp']}F")

lat = data['coord']['lat']
lon = data['coord']['lon']

resp = req.get(
    "http://api.openweathermap.org/data/2.5/onecall",
    params={
        "appid": key,
        "lat": lat,
        "lon": lon,
        "units": "imperial"
    }
)

# print(resp.text)
