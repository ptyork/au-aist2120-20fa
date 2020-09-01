#import random
from random import randint

'''
name:       roll_die
params:     none
returns:    the result of a single six sided die roll
'''
def roll_die():
    # roll = random.randint(1,6)
    roll = randint(1,6)
    return roll


'''
name:       roll_dice
params:     num_rolls
retuns:     the sum of num_rolls random six-sided dice rolls
'''
def roll_dice(num_rolls):
    total = 0
    for i in range(num_rolls):
        roll = randint(1,6)
        total += roll
    
    return total



r1 = roll_die()
print(1)
r2 = roll_die()
print(r2)
r3 = roll_die()
print(r3)
r4 = roll_die()
print(r4)
print(r1+r2+r3+r4)


rolls = roll_dice(2)
print(rolls)
