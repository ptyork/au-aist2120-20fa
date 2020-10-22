# METHOD 1, IMPORT ENTIRE MODULE INTO ISOLATED NAMESPACE
# import module_1022

# module_1022.say_hi('Paul')

# print(module_1022.content)


# METHOD 2, IMPORT ALL MODULE VARIABLES AND FUNCTIONS INTO CURRENT NAMESPACE
# DANGER WILL ROBINSON
# from module_1022 import *
# print(content)
# say_hi('john')


import logging as log

log.basicConfig(
    level=log.DEBUG,   # Show this level or above
    format='%(asctime)s -  %(levelname)s - %(message)s',
    filename='imports_1022.log'
    )

log.debug('in imports_1022 - ' + __name__)

from module_1022 import say_hi
from module_1022 import content as hstring

say_hi('george')
print(hstring + 'BOOM!')

val = hstring + '3'

print(val)
