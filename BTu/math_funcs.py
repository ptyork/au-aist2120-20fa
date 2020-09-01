from funcs_901 import get_int

'''
name:       get_summation
params:     max_n
returns:    the summation from 1 to max_n
'''
def get_summation(max_n):
    total = 0
    for i in range(1, max_n + 1):
        total += i
    
    return total




############################

summ = get_summation(5)
print(summ)

num = get_int("Enter a num to sum: ")
summ = get_summation(num)
print(summ)

