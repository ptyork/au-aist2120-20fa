'''
name:       get_summation
params:     max_n
returns:    the summation of n from 1 to max_n
'''
def get_summation(max_n):
    try:
        total = 0
        for n in range(1, max_n + 1):
            total += n  # total = total + n

        return total
    except:
        print("BAD STUFF HAPPENED")
        return -1


summ = get_summation(5)
print(f"The summation of 5 is {summ}")
summ = get_summation(4)
print(f"The summation of 4 is {summ}")
summ = get_summation(10)
print(f"The summation of 10 is {summ}")
summ = get_summation("100")
print(f"The summation of 5 is {summ}")
