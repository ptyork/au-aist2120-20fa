
name = "paul"
name = "paulie"

# IMMUTABLE MEANS CANNOT BE CHANGED
# STRINGS ARE IMMUTABLE

name = "   Paul  yoRK  "
print(name)
name = name.strip()   # lstrip() / rstrip()
print(name)
name = name.upper()
print(name)
name = name.lower()
print(name)
name = name.capitalize()
print(name)
name = name.title()
print(name)


while True:
    name = input("Enter your name: ")
    name = name.strip()
    name = name.title()
    if len(name) > 0:
        break
    else:
        print("YOU SUCK!!!")

print(f"Hi there, {name}")

