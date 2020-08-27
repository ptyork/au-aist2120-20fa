
print('counter control')

counter = 0

while counter < 10:
    print("Number " + str(counter))
    counter += 1   # counter = counter + 1

##################################

# for (int counter=0; counter < 10; counter++
# foreach (var student in class)

for c in range(10):  # range creates a list of nums from 0 to 9
    print("Number " + str(c))
    print("Number",c)
    # Console.WriteLine($"{name} is awesome");
    # string interpolation
    print(f"Number {c}")

##################################
# FROM 1 TO 10

counter = 0

while counter < 10:
    counter += 1   # counter = counter + 1
    print("Number " + str(counter))

##################################

for c in range(10):  # range creates a list of nums from 0 to 9
    print(f"Number {c+1}")

##################################

print("SUMMATION OF N FROM 1 TO 15")

n = 1
subtotal = 0       # accumulator
while n <= 15:
    print(f"{subtotal} + {n} = {subtotal + n}")
    subtotal = subtotal + n
    n += 1    # n = n + 1

print(f"TOTAL: {subtotal}")

##################################

n = 1
subtotal = 0       # accumulator
while n <= 15:
    print(f"{subtotal} + {n} = ", end="")
    subtotal = subtotal + n
    n += 1    # n = n + 1
    print(subtotal)

print(f"TOTAL: {subtotal}")

##################################

print ("FIBONACCI")

counter = 0
a = 1
b = 1
print("1: 1\n2: 1")
while counter < 8:
    counter += 1   # COUNTER IS ONLY FOR REPITITION
    newval = a + b
    a = b
    b = newval
    print(f"{counter + 2}: {b}")
print(f"FINAL VALUE: {b}")
