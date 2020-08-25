#######################################

counter = 0

while counter < 10:
    print("Number " + str(counter + 1))
    #counter = counter + 1
    counter += 1

#####################################

# for (int c = 0; c < 10; c++) { ... }
for c in range(10):
    # print("Number " + str(c + 1))
    # print("Number", c + 1)
    print(f"Number {c + 1}")   # F-STRINGS ROCK!!!!! (string interpolation)

#############################################

print('SUMMATION from 1 to 8 of n')

n = 1
summ = 0    # accumulator variable

while n <= 8:     # 1 to 8 INCLUSIVE OF 8
    print(f"{summ} + {n} = {summ + n}")
    summ = summ + n
    n += 1

print(summ)

#############################################

print('SUMMATION from 1 to 8 of n (part deux)')

n = 1
summ = 0    # accumulator variable

while n <= 8:     # 1 to 8 INCLUSIVE OF 8
    print(f"{summ} + {n} = ", end="")
    summ = summ + n
    print(summ)
    n += 1

print(summ)

######################################

print("FIRST 12 FIBONACCI")

counter = 0
old = 1
older = 1
print("1\n1")
while counter < 10:
    newval = old + older
    older = old
    old = newval
    print(newval)
    counter += 1







