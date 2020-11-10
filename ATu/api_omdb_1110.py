import json
import requests as req
from pprint import pprint as pp
import sys

with open('\\apikeys.json') as fi:
    apikeys = json.loads(fi.read())

key = apikeys["OMDB"]

if len(sys.argv) < 2:
    print('MUST SUPPLY A MOVIE TITLE')
    exit()

title =' '.join(sys.argv[1:])

resp = req.get(
    "http://www.omdbapi.com/",
    params={
        "apikey": key,
        "t": title
    }
)

# print(resp.text)
data = json.loads(resp.text)

print(f"{data['Title']} has a rating of {data['Rated']}")

ratings = data['Ratings']

for rating in ratings:
    src = rating['Source']
    val = rating['Value']
    print(f" * {src}: {val}")

posterUrl = data['Poster']

resp = req.get(posterUrl)

# Copied from common\scraping\web_requests.py
def save(filename, rsp):
    with open(filename, 'wb') as file:
        for bytes in rsp.iter_content(10000):
            file.write(bytes)

save(data['Title'] + ' Poster.jpg', resp)
