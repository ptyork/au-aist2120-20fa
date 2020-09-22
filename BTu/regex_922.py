'''
paul@yorkfamily.com
pyork1@augusta.edu
paul.york@augusta.edu
ptyork@cc.gatech.edu
pyork@someplace.co.uk

baddie.arse@poo
dude,place
@dude
a@b,c
.@@@
'''

def isEmailOldWay(addr):
    # if '@' not in addr:
    #     return False
    # if '.' not in addr:
    #     return False
    # if addr[-3] != '.' and addr[-4] != '.':
    #     return false
    addr_parts = addr.split('@')
    if len(addr_parts != 0):
        return False
    name = addr_parts[0]
    domain = addr_parts[1]
    domain_parts = domain.split('.')
    if len(domain_parts) < 2:
        return False
    return True


'''
REGULAR EXPRESSIONS

CHARACTER CLASSES:
.       Wildcard ... matches anything
\w      "Word" character ([a-zA-Z0-9_])
\d      "Digit" characters ([0-9])
\s      "Whitespace" characters
\S      NOT "Whitespace" characters

CUSTOM CHARACTER CLASS (by default case sensitive)
[Aa]    "A" or "a"
[ABCabc] "A", "B", "C", "a", "b" or "c"
[A-F]    "A" or "B" or ... or "F"
[0-9]   0,1,2,3,...,9
[a-zA-Z0-9_]        (equivalent to \w)
[^A-Z]      NOT between "A" and "Z"


QUANTIFIERS:
c+      Matches 1 or more "c's"
c?      Matches 0 or 1 c's
c*      Matches 0 or many c's
c{x}    Matches exactly x c's
c{x,}   Matches x or more c's (inclusive)
c{x,y}  Matches between x and y c's (inclusive)
c{,y}   Matches less than y c's (inclusive)

MISCELLANEOUS:
()      Grouping operators
(a1|a2) Alternatives
(a1|a2|a3|...)  (as many as you like)

'''

import re

def isEmail(addr):
    # test = re.compile(r'\w+(\.\w+)*@(\w+)(\.\w+)+')
    # test = re.compile(r'[a-z0-9_+.]{3,}@(\w+)(\.\w+)+')
    # test = re.compile(r'[a-z0-9_+.]{3,}@(\w{2,})(\.\w{2,})+')
    # test = re.compile(r'[a-zA-Z0-9_+.]{3,}@(\w{2,})(\.\w{2,})+')
    test = re.compile(r'[a-z0-9_+.]{3,}@(\w{2,})(\.\w{2,})+', re.IGNORECASE)
    res = test.fullmatch(addr)
    if res == None:
        return False
    else:
        return True


def isPhone(num):
    test = re.compile(r'(\(\d{3}\)|\d{3})[ .-]?\d{3}[ .-]?\d{4}')
    res = test.fullmatch(num)
    if res == None:
        return False
    else:
        return True


# isEmail('a@b.c')

allmails = '''
paul@yorkfamily.com
pyork1@augusta.edu
paul.york@augusta.edu
ptyork@cc.gatech.edu
pyork@someplace.co.uk
pyork@gmail.com
pyork+nospam@gmail.com
a@b.c
paul@b.c
PAUL.YORK@AUGUSTA.EDU

baddie.arse@poo
dude,place
@dude
a@b,c
.@@@
'''

emails = allmails.split()
# print(emails)
for email in emails:
    res = isEmail(email)
    print(f"{email}:\t{res}")
