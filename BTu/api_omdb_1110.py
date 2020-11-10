import json
import requests as req
from pprint import pprint as pp
import sys

with open('\\apikeys.json') as fi:
    apikeys = json.loads(fi.read())

key = apikeys["OMDB"]

# print(sys.argv)
# print(sys.argv[1:])
# print(' '.join(sys.argv[1:]))
name = ' '.join(sys.argv[1:])

resp = req.get(
    "http://www.omdbapi.com/",
    params={
        "apikey": key,
        "t": name
    }
)

# print(resp.text)

data = json.loads(resp.text)

# pp(data)

title = data['Title']
plot = data['Plot']
rating = data['Rated']
year = data['Year']
runtime = data["Runtime"]
total_mins = int(runtime.split()[0])
hours = total_mins // 60
mins = total_mins % 60

reviews = data['Ratings']

print(f"{title} from {year} is rated {rating}")
print(plot)
print(f"RUNTIME: {hours}:{mins:02}")

for review in reviews:
    src = review["Source"]
    val = review["Value"]
    print(f" * {src}: {val}")

posterUrl = data['Poster']

# print(posterUrl)

# Generic way of saving a web file
def save(filename, rsp):
    with open(filename, 'wb') as file:
        for bytes in rsp.iter_content(10000):
            file.write(bytes)

resp = req.get(posterUrl)

if resp.headers["CONTENT-TYPE"] == "image/jpeg":
    save(title + " Poster.jpg", resp)
elif resp.headers["CONTENT-TYPE"] == "image/png":
    save(title + " Poster.png", resp)
else:
    print("BAD IMAGE")
