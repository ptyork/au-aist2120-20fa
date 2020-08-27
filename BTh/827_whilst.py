
counter = 0

while counter < 20:
    print("Number " + str(counter))
    counter += 1     # counter = counter + 1

###############################################

# for (int counter = 0; counter < 20; counter++) { ... }
# foreach (string name in students) { ... }

for c in range(20):
    print("for Number " + str(c))
    print("for Number", c)
    # string interpolation????
    # $"{name} is awesome"
    print(f'{c} is the number')

################################################

counter = 0

while counter < 20:
    counter += 1     # counter = counter + 1
    print("Number " + str(counter))

###############################################

# for (int counter = 0; counter < 20; counter++) { ... }
# foreach (string name in students) { ... }

for c in range(20):
    print(f'{c+1} is the number')

################################################

n = 1
subtotal = 0

while n <= 10:
    # print(f"{subtotal} + {n} = {subtotal + n}")
    print(f"{subtotal} + {n} = ", end="")
    subtotal = subtotal + n    # subtotal += n
    print(subtotal)
    n += 1

print(f"The sum is {subtotal}")

#######################################################

counter = 0
a = 1
b = 1
print('1: 1\n2: 1')
while counter < 8:
    counter += 1
    summ = a + b
    a = b
    # b = a + b # summ WHY NOT???
    b = summ
    print(f"{counter+2}: {b}")

##print(summ)
