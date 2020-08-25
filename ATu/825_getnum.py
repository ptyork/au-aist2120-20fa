
while True:
    numstr = input("ENTER A NUMBER: ")
    numstr = numstr.strip()
    if numstr.isnumeric():
        num = int(numstr)
        break
    else:
        print("I SAID A NUMBER YOU NUMSKULL!")

print(f"You entered {num}")
