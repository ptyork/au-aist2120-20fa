import json
import requests as req
from pprint import pprint as pp
import sys

# print(sys.argv)
# print(sys.argv[1:])
# print(' '.join(sys.argv[1:]))
movie_name = ' '.join(sys.argv[1:])

with open('\\apikeys.json') as fi:
    apikeys = json.loads(fi.read())

key = apikeys["OMDB"]

resp = req.get(
    "http://www.omdbapi.com/",
    params={
        "apikey": key,
        "t": movie_name
    }
)

movie = json.loads(resp.text)

# pp(movie)

title = movie["Title"]
rated = movie["Rated"]
year = movie["Year"]
released = movie["Released"]
runtime = movie["Runtime"]  # '111 mins'

total_mins = int(runtime.split()[0]) # 111
hours = total_mins // 60
mins = total_mins % 60

# print(f"{title} has a MPAA rating of {rated} and was released on {released} and has a runtime of {runtime}")
print(f"{title} has a MPAA rating of {rated} and was released on {released} and has a runtime of {hours}:{mins}")

ratings = movie["Ratings"]
for rate_dict in ratings:
    src = rate_dict["Source"]
    val = rate_dict["Value"]
    print(f" * {src}: {val}")

print(f" * Metascore: {movie['Metascore']}")
