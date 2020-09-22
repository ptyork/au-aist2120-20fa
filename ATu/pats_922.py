'''
pyork1@augusta.edu
paul.york@augusta.edu
paul@yorkfamily.com
paul@something.co.uk

@.@x@
'''

def isEmailBadWay(addr):
    # if '@' in addr and 
    #    '.' in addr and 
    #    addr[-4] == '.':
    #     return True 
    # else:
    #     return False
    parts = addr.split('@')
    if len(parts) != 2:
        return False
    domain = parts[1]   # 'augusta.edu'
    domain_parts = domain.split('.')  # ['augusta', 'edu']
    if len(domain_parts) < 2:
        return False
    return True



'''
REGULAR EXPRESSIONS:
Pattern Rules:

CHARACTER CLASSES:
"SPECIAL" classes:
\w == One "Word Character" a-z A-Z 0-9
\d == One "Digit" Character 0-9
\s == One "Space" Character (whitespace)
\S == One "NOT a SPACE" Character
.  == ONE of ANYTHING (wildcard)

"CUSTOM" character class:
[Aa]     explicit characters
[ABC]    explicit character list
[A-C]    character range
[a-cA-C] multiple ranges
[0-9]    same as \d
[0-9A-Fa-f]   Happens to be a Hex digit

QUANTIFIERS:
c{#}  == find exactly "#" chars
c{#,}  == find "#" or more chars
c{,#}  == find at most "#" chars
c{x,y} == find between x and y (inclusive) chars
c+    == find 1 or more c
c*    == find 0 or more c
c?    == find 0 or 1 c

MISCELLANEOUS:
Parens around a pattern form a "group"
  - can allow for quantifier at the group level
  - can also "match" individual groups (useful later)
  - e.g.,   (\d{1,3})(\.\d{1,3}){3}   == matches 123.123.123.123
Pipe denotes ALTERNATIVES 
  - (patt1|patt2|patt3)   Match one or the other or the other
  - e.g.,  \d{3}|\(\d{3}\)  == matches 123 OR (123)

CSS Example:
[0-9A-Fa-f]         == hex digit
#[0-9A-Fa-f]{6}     == 6 digit hex color in CSS (starts with #)
#([0-9A-Fa-f]{3}|[0-9A-Fa-f]{6})    == 3 OR 6 digit hex color

'''
import re   # regular expression library

def isEmail(addr):
    # test = re.compile(r'\S+@(\w+)(\.\w+)+')
    # test = re.compile(r'[a-z._0-9]+@(\w+)(\.\w+)+', re.IGNORECASE)
    test = re.compile(r'[a-z._0-9]+@(\w{2,})(\.\w{2,})+', re.IGNORECASE)
    m = test.match(addr)
    if m == None:
        return False
    else:
        return True


def isPhone(num):
    test = re.compile(r'(\d{3}|\(\d{3}\))[ .-]?(\d{3})[ .-]?(\d{4})')
    m = test.match(num)
    if m == None:
        return False
    else:
        return True


####### TESTS #######

emailstr = '''
pyork1@augusta.edu
paul.york@augusta.edu
paul@yorkfamily.com
paul@something.co.uk
bubbaWuz@here
paul,is,@place.org
PAUL@YORKFAMILY.COM
a@b.c
'''

emails = emailstr.split()   # convert to list of emails
print(emails)

for email in emails:
    isit = isEmail(email)
    print(f"{email}\t{isit}")


