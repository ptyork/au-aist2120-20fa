'''
paul@yorkfamily.com
paul.york@augusta.edu
pyork1@augusta.edu
ptyork@cc.gatech.edu
ptyork@marchfirst.co.uk
PAUL.YORk@auGUsta.edu
paul@yorkfamily_com
a@b.c
j,,@@
j..@..com
I am not an email
paul york@augusta university.edu
paul@yorkfamily,.com
paul,york@augusta.edu
,@@_._
'''

def isEmailOld(addr):
    # if '@' not in addr:
    #     return False
    # if '.' not in addr:
    #     return False
    # if ' ' in addr:
    #     return False
    addr_parts = addr.split('@')
    if len(addr_parts) != 2:
        return False
    name = addr_parts[0]
    domain = addr_parts[1]
    if len(name)<2:
        return False
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
.       Match ANY character (wildcard)
\w      Match any WORD character [A-Za-z0-9_]
\d      Match any DIGIT character [0-9]
\s      Match any WHITESPACE character (space, newline, tab)
\S      Match any NOT WHITESPACE character
(custom)
[]      List of chars in brackets
[ABab]  A, B, a, b
[C-F]   C,D,E,F
[3-7]   3,4,5,6,7
[A-Za-z0-9_]    Same as \w
[0-9]   Same as \d
[ -.]
[ .-]
[^0-9]  NOT a digit


Quantifiers  (char + quantifier OR group + quantifier):
+       Match 1 or more of the char
*       Match 0 or more of the char
?       Match 0 or 1 of the char
(custom)
{m}     Match m of the char
{m,n}   Match BETWEEN m and n chars (INCLUSIVE)
{m,}    Match AT LEAST m chars
{,n}    Match AT MOST n chars


Special Rules:
Escape special characters with a \
Use () to form groups
Alternative pattern choices can be separated by a |
(a|an|the|or)


'''
import re

def isEmail(addr):
    # tst = re.compile(r'[A-Za-z0-9_.]+@\w+\.\w+')
    # tst = re.compile(r'[A-Za-z0-9_.]+@(\w+)(\.\w+)+')
    # tst = re.compile(r'[A-Za-z0-9_.]{2,}@(\w{2,})(\.\w{2,})+')
    # tst = re.compile(r'\w[A-Za-z0-9_.]*\w@(\w{2,})(\.\w{2,})+')
    tst = re.compile(r'\w[a-z0-9_.]*\w@(\w{2,})(\.\w{2,})+', re.IGNORECASE)
    res = tst.fullmatch(addr)
    if res == None:
        return False
    else:
        return True
    # return res != None
    # return not res

def isPhone(num):
    tst = re.compile(r'(\d{3}|\(\d{3}\))[ -.]?\d{3}[ -.]?\d{4}')
    res = tst.fullmatch(num)
    if res == None:
        return False
    else:
        return True


# print(isEmail('paul@yorkfamily.com'))
# print(isEmail('paul,york@augusta.edu'))

all_addresses = '''
paul@yorkfamily.com
paul.york@augusta.edu
pyork1@augusta.edu
ptyork@cc.gatech.edu
ptyork@marchfirst.co.uk
PAUL.YORk@auGUsta.edu
paul@yorkfamily_com
a@b.c
j,,@@
j..@..com
I am not an email
paul york@augusta university.edu
paul@yorkfamily,.com
paul,york@augusta.edu
,@@_._
.paul@yorkfmaily.com
paul.@augusta.edu
'''

addrs = all_addresses.splitlines()
# print(addrs)
for addr in addrs:
    if len(addr) == 0:
        continue
    res = isEmail(addr)
    print(f"{addr:50}{res}")
