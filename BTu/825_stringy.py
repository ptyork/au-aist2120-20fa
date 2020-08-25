
# STRING METHODS
# (NOTE: string are immuatble)
# strip() / lstrip() / rstrip()

a = "   hello  world   "
a = a.strip()
print(a)

# capitalize() / upper() / lower() / title()
print(a.capitalize())
print(a)    # a DOES NOT CHANGE WHEN I CALL A STRING METHOD
print(a.upper())
print(a.lower())
print(a.title())

# len()    NOT A STRING METHOD

while True:
    name = input("Enter you name: ")
    name = name.strip()
    if (len(name) > 0):
        break
    else:
        print("Dumbass!!")

print(f"Hello {name}")



