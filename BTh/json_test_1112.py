from pprint import pprint as pp
import json

me_dict = {
    "Name": "Paul",
    "Age": 48
}

print(me_dict)
pp(me_dict)

js = json.dumps(me_dict)
print(js)

my_list = [10,20,15,17,19]
print(my_list)
pp(my_list)

js = json.dumps(my_list)
print(js)


me_dict = {
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
            "Age": 9
        }
    ]
}

# print(me_dict)
pp(me_dict)

js = json.dumps(me_dict, indent=4)
print(js)


# Save JSON to file
with open('me.json', 'wt') as jfile:
    jfile.write(js)


# LOAD JSON from file
with open('me.json', 'rt') as jfile2:
    me_json = jfile2.read()

other_me_dict = json.loads(me_json)

pp(other_me_dict)

print(other_me_dict["Name"])
print(other_me_dict["Spouse"])
spouse = other_me_dict["Spouse"]
print(spouse["Name"])
print(other_me_dict["Spouse"]["Name"])
print(other_me_dict["Kids"][1]["Name"])
print(other_me_dict["Kids"][0]["Age"])
