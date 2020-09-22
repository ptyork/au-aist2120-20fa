# String literal
a = "ABC"
b = 'DEF'
ml = '''This is a very long string
that takes up multiple
lines and ends with a'''

# F STRING
f''
f""
f''' '''

two_lines = "line 1 \n line 2"
one_line_with_tabs = "\t\tname\tphone"
next_line = "\t\tPaul\t555-1212"
print(one_line_with_tabs)
print(next_line)

# RAW STRING
path = r"c:\windows\system32\user.dll"
print(path)

name = 'SHOPPING CART'

# STRING FUNCTIONS
print(ml.count('a'))
print(ml.count('and'))

# - searching
print('and' in ml)
print('and' not in ml)
print(ml.startswith('This'))
print(ml.endswith('multiple'))
print(ml.find('and'))  # ml.index('and') is the same except for the exception

# - formatting
print('FORMATTING')
print(name.center(80))
print('SUBTOTAL'.rjust(80))

h1 = 'PRODUCT'
h2 = 'QTY'
h3 = 'PRICE'
h4 = 'SUBTOTAL'

# (alignment)(spaces)(separator)(data type)
print('{:^80}'.format(name))     # EQUIVALENT TO print(name.center(80))
header = '{:<40}{:>15}{:>15}{:>10}'.format(h1, h2, h3, h4)
print(header)

print('\n\n')
header = f"{h1:<40}{h2:>15}{h3:>15}{h4:>10}"
print(f"{name:^80}")
print(header)

product = "Cheerios"
qty = 3
price = 3.90
subtotal = qty * price

print(f"{product:40}{qty:>15}{price:>15.2f}{subtotal:>10.2f}")

num = 5572945.8964658
print(f"{num}")
print(f"{num:.3f}")
print(f"{num:.4f}")
print(f"{num:,.4f}")
print(f"{num:^20,.4f}")

# STRINGS ARE SEQUENCES OF CHARACTERS

for c in 'HELLO':
    print(c)

s = "Now is the time for all good men to come to the aid of their country"

print(len(s))
print(s[::-1])
rev = reversed(s)
revlist = list(rev)
print(revlist)
strlist = list(s)
print(strlist)

# PUT A STRING BACK TOGETHER AGAIN
print(''.join(strlist))

words = s.split()
print(words)

for word in words:
    print(word.capitalize(), end=' ')
print()
