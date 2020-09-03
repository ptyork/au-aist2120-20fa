#import random
# random.randint(1,6)
from random import randint
# randint(1,6)

'''
name:       roll_die
params:     none
returns:    a 6-sided die roll
'''
def roll_die():
    roll = randint(1, 6)
    return roll

'''
name:       roll_dice
params:     num_rolls
returns:    the sum of num_rolls rolls
'''
def roll_dice(num_rolls):
    total = 0
    for i in range(num_rolls):
        total = total + roll_die()

    return total

my_roll = roll_die()
print(f"I rolled a {my_roll}")

d1 = roll_die()
d2 = roll_die()
d3 = roll_die()
d4 = roll_die()
print(f"4 rolls total {d1+d2+d3+d4}")

# THESE ARE DIFFERENT

# d1 = roll_die()
# d2 = roll_die()

# d12 = randint(2,12)

d1234 = roll_dice(4)
print(f"4 rolls total {d1234}")

d6 = roll_dice(6)
print(f"6 rolls total {d6}")

