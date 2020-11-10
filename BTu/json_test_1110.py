from pprint import pprint as pp
import json

me = {
    "Name": "Paul",
    "Age": 48,
    "IsAwesome": True,
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

# print(me["Name"])
# print(me["Spouse"]["Name"])
# print(me["Kids"][1]["Name"])

# pp(me)

text = json.dumps(me, indent=4, sort_keys=True)
# print(text)

# TO SAVE TO DISK
with open('test.json', 'wt') as file_one:
    file_one.write(text)

# TO LOAD FROM DISK
with open('test.json', 'rt') as file_two:
    jdata = json.loads(file_two.read())

pp(jdata)

print(jdata["Name"])
print(jdata["Spouse"]["Name"])
print(jdata["Kids"][1]["Name"])
