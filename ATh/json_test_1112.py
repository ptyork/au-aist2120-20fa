from pprint import pprint as pp
import json

me_dict = {
    "Name": "Paul",
    "Age": 48,
    "Spouse": {
        "Name": "Meredith",
        "Age": 29
    },
    "Kids": [
        {
            "Name": "Keaton",
            "Age": 9
        },
        {
            "Name": "Kylie",
            "Age": 13
        }
    ]
}

my_grades = [
    77,
    84,
    97,
    30
]



print(me_dict)
print(my_grades)

pp(me_dict)
pp(my_grades)

js = json.dumps(me_dict)
print(js)

js2 = json.dumps(my_grades)
print(js2)

js = json.dumps(me_dict, indent=4)
print(js)

# SAVE JSON TO DISK
with open('me.json', 'wt') as jsf:
    jsf.write(js)


# READ AND CONVERT JSON FROM DISK
with open('me.json', 'rt') as jsf:
    text = jsf.read()

me_from_disk = json.loads(text)

pp(me_from_disk)

print(me_from_disk["Name"])  # my name
print(me_from_disk["Spouse"]["Name"]) # wife's name
print(me_from_disk["Kids"][1]["Name"]) # second kid's name
print(me_from_disk["Kids"][0]["Age"]) # first kid's age
