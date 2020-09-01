#import random
from random import randint

'''
name:       roll_die
params:     none
returns:    the value of a singe 6-sided die roll
'''
def roll_die():
    roll = randint(1,6)
    return roll

'''
name:       roll_dice
params:     count
returns:    the value of count 6-sided die rolls
'''
def roll_dice(count):
    total = 0
    for n in range(count):
        roll = randint(1,6)
        total += roll
    return total



my_roll = roll_die()
print(f"I rolled a {my_roll}")

my_roll = roll_dice(1)
print(f"I rolled a {my_roll}")

my_roll = roll_dice(5)
print(f"I rolled a {my_roll}")

