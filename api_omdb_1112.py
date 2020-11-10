import json
import requests as req
from pprint import pprint as pp

with open('\\apikeys.json') as fi:
    apikeys = json.loads(fi.read())

key = apikeys["OMDB"]

resp = req.get(
    "http://www.omdbapi.com/",
    params={
        "apikey": key,
        "t": ""
    }
)
