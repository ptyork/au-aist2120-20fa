
while True:
    numstr = input("Enter a number: ").strip()
    #numstr = numstr.strip()
    if numstr.isnumeric():
        break
    else:
        print("YOU NUMBNUTS!!")

num = int(numstr)
print(f"You entered {num}")
