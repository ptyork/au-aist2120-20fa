#import random
from random import randint

'''
name:       get_roll
params:     none
returns:    the value of one 6-sided die roll
'''
def get_roll():
    roll = randint(1,6)
    return roll


'''
name:       get_rolls
params:     num_rolls
returns:    the value of num_rolls rolls
'''
def get_rolls(num_rolls):
    total = 0
    for i in range(num_rolls):
        total += get_roll()
    return total

#random.randint(1,6)

my_roll = get_roll()
print(f"I rolled a {my_roll}")

r1 = get_roll()
r2 = get_roll()
r3 = get_roll()
r4 = get_roll()
print(f"4 dice = {r1+r2+r3+r4}")

rolls = get_rolls(6)
print(f"6 dice = {rolls}")
