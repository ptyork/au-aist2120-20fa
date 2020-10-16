# boolean expression
# True or False (also on or off, 1 or 0, yes or no)

# Boolean Operators
# Must be over 21 and not infected with covid
#    AND
#  BOTH OPERANDS MUST BE TRUE IN ORDER FOR THE EXPRESSION TO BE TRUE
#    C#:     &&
#    Python: and

print("AND")
print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False


# Must be uninfected or asymptomatic
#    OR
#  EITHER (OR BOTH) OPERANDS MUST BE TRUE IN ORDER FOR THE EXPRESSION TO BE TRUE
#    C#:     ||
#    Python: or

print("OR")
print(True or True)   # True
print(True or False)  # True
print(False or True)  # True
print(False or False)  # False


# COMPARISON OPERATORS

# EQUALITY
#   = vs ==
print("==")
print(True == False)   # False
print(True == True)    # True

# INEQUALITY
print("!=")
print(True != True)    # False
print(True != False)   # True

# GT OR LT
#  > for Greater Than
#  < for Less Than
#  >= for GT or Equal
#  <= for LT or Equal

# C#
# if (a > b)
# {
#     DO SOMETHING;
#     DO SOMETHING;
#     DO SOMETHING;
# }

a = 1
b = 2
if a < b:
    print('yes it is')
    print('aren\'t I grand')
    if a == 1:
        print('a is so boring')
    print('b is so boring')
print('all done')

age = 19
iscool = True

if age >= 21 and iscool == True:
    print('come in')
else:
    print('nice try')

if age >= 21 and iscool == True:
    print('come in')
elif age >= 21 and iscool == False:
    print('stand in the dork line')
else:
    print('nice try')

# NOT OPERATOR  (in C# it was !)
# not True ==> False
# not False ==> True

if age >= 21 and iscool:
    print('come in')
elif age >= 21 and not iscool:
    print('stand in the dork line')
else:
    print('nice try')


age = 12

while age < 21:
    print('go home little kid')
    # age = age + 1
    age += 1

print('come on in')

# break
# continue    

counter = 0
while True:
    print('hello')
    counter += 1
    if (counter > 5):
        break


# for loop????????? (book give for in range())
