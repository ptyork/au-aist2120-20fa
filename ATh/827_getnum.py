while True:
    numstr = input("Enter a number: ")
    numstr = numstr.strip()

    if numstr.isnumeric():
        break
    else:
        print("NOPE!!!")

num = int(numstr)
print(f"You entered {num}")
