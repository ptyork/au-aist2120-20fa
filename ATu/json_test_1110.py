import json
from pprint import pprint as pp

me = {
    "Name": "Paul",
    "Age": 48,
    "Spouse": {
        "Name": "Meredith",
        "Age": 29
    },
    "Kids": [
        {
            "Name": "Kylie",
            "Age": 13
        },
        {
            "Name": "Keaton",
            "Age": 8
        }
    ]
}

# pp(me["Kids"])
# print(me["Kids"][0]["Age"])

text = json.dumps(me, indent=4)
print(text)










