'''
paul@yorkfamily.com
paul.york@augusta.edu
pyork1@augusta.edu
ptyork@cc.gatech.edu
bubba@ll.co.uk


paul york@dodos are.extinct
paul@york.
.@.
.#

'''

def isEmailOld(addr):
    # if '@' not in addr:
    #     return False
    # if '.' not in addr:
    #     return False
    # if addr.count('@') != 1:
    #     return False
    addr_parts = addr.split('@')   # ['name', 'domain.com']
    if len(addr_parts) != 1:
        return False
    name = addr_parts[0]
    domain = addr_parts[1]
    domain_parts = domain.split('.')
    if len(domain_parts) < 2:
        return False
    for part in domain_parts:
        if len(part) < 2:
            return False
    
    return True


'''
REGULAR EXPRESSION SYNTAX

Character Classes:
.       Match ANY character
\w      Match any WORD character [A-Za-z0-9_]
\d      Match any DIGIT character [0-9]
\s      Match any whitespace character
\S      Match and NON whitespace character
(Custom)
[Aa]    Capital or lower A
[A-C]   (Range) A, B or C
[a-c]
[A-Ca-c]  Compound range
[0-7]   0,1,2,3,4,5,6,7
[^0-9 _] Anything BUT 0 to 9, space or underscore

Quantifiers (after any character class or group):
+       Match 1 or more of the chars
*       Match 0 or more of the chars
?       Match 0 or 1 of the chars
(Custom)
{m}     Match EXACTLY m of the chars
{m,n}   Match BETWEEN m and n of the chars (INCLUSIVE)
{m,}    Match m or MORE of the chars
{,n}    Match UP TO n of the chars

Rules:
Special characters can be escaped with a preceding \
Groups can be created with ()
Alternative options are separated with the | character
(and|or)
(and|or|but)
'''

import re

def isEmail(addr):
    # tst = re.compile(r'\w+@\w{2,}\.\w{2,}')
    # tst = re.compile(r'\S+@\w{2,}\.\w{2,}')
    # tst = re.compile(r'[A-Za-z0-9._]+@\w{2,}\.\w{2,}')
    # tst = re.compile(r'\w[A-Za-z0-9._]*\w@\w{2,}\.\w{2,}')
    # tst = re.compile(r'\w[A-Za-z0-9._]*\w@(\w{2,})(\.\w{2,})+')
    tst = re.compile(r'\w[a-z0-9._]*\w@(\w{2,})(\.\w{2,})+', re.IGNORECASE)
    res = tst.fullmatch(addr)
    if res == None:
        return False
    else:
        return True
    # return tst.search(addr)

def isPhone(num):
    tst = re.compile(r'(\d{3}|\(\d{3}\))[ .-]?\d{3}[ .-]?\d{4}')
    res = tst.fullmatch(num)
    if res == None:
        return False
    else:
        return True


# print(isEmail('paul@yorkfamily.com'))
# print(isEmail('paul.york@augusta.edu'))

all_addresses = '''
paul@yorkfamily.com
paul.york@augusta.edu
pyork1@augusta.edu
ptyork@cc.gatech.edu
bubba@ll.co.uk
PAUL.YORK@augusta.eDU
paul,york@augusta.edu
paul.@augusta.edu
.paul@augusta.edu

paul york@dodos are.extinct
paul@york.
.@.
.#

'''

add_list = all_addresses.splitlines()

for addr in add_list:
    if len(addr) > 0:
        #print(addr)
        res = isEmail(addr)
        print(f"{addr:30}{res}")
