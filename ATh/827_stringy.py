# STRINGS ARE IMMUTABLE
a = "abc"
a = "ABC"

# STRING METHODS

name = "   paul  york   "
name.upper()
print(name)
name = name.upper()
print(name)
name = name.capitalize()
print(name)
name = name.lower()
print(name)
name = name.title()
print(name)

name = name.strip()  # lstrip() / rstrip()
print(name)


############################################

while True:
    name = input("Please enter your name: ")
    name = name.title()
    name = name.strip()
    if len(name) == 0:
        print("YOU ARE STUPID!! I SAID YOUR NAME!!")
    else:
        print(f"Oh, hi {name}")
        break


