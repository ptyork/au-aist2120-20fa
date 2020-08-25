# Basic string methods

# strip()   [ also lstrip and rstrip ]
s = "   la la la   "
s = s.strip()
print(s)

# upper()/lower()/capitalize()/title()
name = "paul york"
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())

# How big is a string (len)

print(len(name))

# name =""
# while len(name) == 0:

while True:
    name = input("Enter your name: ")
    name = name.strip()
    name = name.title()
    if len(name) > 0:
        print(f"Hi {name}")
        break
    else:
        print("YOU SUCK!!")







