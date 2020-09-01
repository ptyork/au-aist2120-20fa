from funcs_901 import get_int_range

'''
name:       get_summation
params:     max_n
return:     summation from 1 to max_n
'''
def get_summation(max_n):
    try:
        total = 0
        for n in range(1, max_n + 1):
            total += n

        return total
    except:
        print("SOMETHING BAD HAPPENED")
        return



###########

summ = get_summation(5)
print(summ)
summ = get_summation(3)
print(summ)
summ = get_summation(1)
print(summ)
summ = get_summation(100)
print(summ)

max_num = get_int_range(1,10)
summ = get_summation(max_num)
print(summ)
