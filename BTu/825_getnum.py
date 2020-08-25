
while True:
    numstr = input("Enter a number: ")
    numstr = numstr.strip()
    if (numstr.isnumeric()):
        num = int(numstr)
        break
    else:
        print("I SAID A NUMBER!!!")

print(f"You entered {num}")
