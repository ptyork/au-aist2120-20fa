# print('hello I am inside of module_1022')

content = "HELLO WORLD FROM MODULE"

def say_hi(name):
    print(f"Hello {name}. Nice to meet you.")

def calc_sum(num1, num2):
    return num1 + num2


def run_unit_test():
    print('TESTING...')
    # run test
    sum = calc_sum(2, 2)
    # assert that it matches my expectations
    # if sum != 4:
    #     blow up
    assert sum == 4

    # run test
    sum = calc_sum(1, 2)
    # assert that it matches my expectations
    assert sum == 3

    print('ALL IS WELL!!')


# print('in module_1022 - ' + __name__)
if __name__ == "__main__":
    run_unit_test()
