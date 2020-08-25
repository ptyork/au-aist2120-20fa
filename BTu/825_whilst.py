###########################################

counter = 0
while counter < 20:
    print("Number is " + str(counter + 1))
    #counter = counter + 1
    counter += 1

###########################################

# for (int counter = 0; counter < 20; counter++)
# foreach (var person in people)

for c in range(20):
    print("Number is " + str(c + 1))
    print("Number is", c+1)
    # $"{name} is great!!" C# string interpolation
    print(f"Number is {c+1}")   # python string interpolation
    # I LOVE F-STRINGS

###########################################

print("SUMMATION FROM 1 TO 20")

n = 1
summ = 0      # accumulator

while n <= 20:
    print(f"{summ} + {n} = {summ + n}")
    summ = summ + n
    n += 1
print(summ)

###########################################

print("SUMMATION FROM 1 TO 20 (part 2)")

n = 1
summ = 0      # accumulator

while n <= 20:
    print(f"{summ} + {n} = ", end="")
    summ = summ + n
    print(f"{summ}")
    n += 1
print(summ)

###########################################

print("FIBONACCI TO 12")

counter = 2
older = 1
old = 1

print("1: 1\n2: 1")

while counter < 15:
    counter += 1
    newval = old + older
    older = old
    old = newval
    print(f"{counter}: {newval}")




