import json
import requests as req
from pprint import pprint as pp
import sys

# print(sys.argv)
# print(sys.argv[1:])
# print(' '.join(sys.argv[1:]))
# exit()

name = ' '.join(sys.argv[1:])

with open('\\apikeys.json') as fi:
    apikeys = json.loads(fi.read())

key = apikeys["OMDB"]

resp = req.get(
    "http://www.omdbapi.com/",
    params={
        "apikey": key,
        "t": name
    }
)

movie = json.loads(resp.text)

# pp(movie)

title = movie['Title']
released = movie['Released']
rated = movie['Rated']
runtime = movie['Runtime']

print(f"{title} was released on {released}, is rated {rated} and has a runtime of {runtime}")

ratings = movie['Ratings']
for rating_dict in ratings:
    src = rating_dict['Source']
    val = rating_dict['Value']
    print(f" * {src}: {val}")

print(f" * Metascore: {movie['Metascore']}")
