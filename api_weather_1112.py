import json
import requests as req
from pprint import pprint as pp

with open('\\apikeys.json') as fi:
    apikeys = json.loads(fi.read())

key = apikeys["OpenWeather"]

resp = req.get(
    "http://api.openweathermap.org/data/2.5/weather",
    # "http://api.openweathermap.org/data/2.5/forecast",
    params={
        "appid": key,
        "zip": "30904"
    }
)
print(resp.text)