# functions vs methods
print('hello')
a = 'hello world'
a = a.upper()
# a = upper(a)

# YOU MUST DEFINE A FUNCTION BEFORE YOU CALL IT
# dothat()

# public void doit(string doitwiththis)
def doit(doitwiththis):
    if type(doitwiththis) != str:
        print("incorrect parameter data type")
        return   # implicitly a return None statement
    
    c = doitwiththis.capitalize()
    c = f"DID IT WITH: {c}"
    print(c)

def dothat():
    print('did that!!')
    # lack of return statement is also implicitly a return none statement

print('hello2')

dothat()
doit(a)

doit(42)

b = int('42')

# public int getsum(int a, int b) {
#    ...
#    return value;
# }

def getsum(a, b):
    if type(a) != int or type(a) != float:
        return
    if type(b) != int or type(b) != float:
        return

    ans = a + b
    return float(ans)

x = dothat()
print(x)

# python nas a None "value", NEARLY eqivalent to the C# null "value"

s1 = getsum(1,2)
print(s1)
print(type(s1))

s2 = getsum(1.1, 2.2)
print(s2)
print(type(s2))

s2 = getsum('hello', 'world')


def doA():
    print('A')
    doB()
    print('!A')

def doB():
    print('B')
    print('!B')


doB()

doA()

print('DONE')


###################### SCOPE ##########################

a = 1
b = 2

print(f'in "main": {a} + {b} = {a+b}')

def printsum(a,b):
    print(f"in printsum: {a} + {b} = {a+b}")

printsum(5,5)

print(f'in "main": {a} + {b} = {a+b}')


def pp():
    a = 5
    b = 6
    print(f"in pp: {a} + {b} = {a+b}")


pp()

print(f'in "main": {a} + {b} = {a+b}')


def pq():
    global a
    global b
    b = 20
    print(f"in pq: {a} + {b} = {a+b}")


pq()

print(f'in "main": {a} + {b} = {a+b}')


def getsumEx(a, b):
    try:
        ans = a + b
        return float(ans)
    except ValueError:
        print('this only works with numbers')
    except:
        print("huh?? I don't know what you're doing.")

print(getsumEx('hello', 'world'))
print(getsumEx(1,2))
print(getsumEx(1.5,2.5))
print(getsumEx('hello', 7))
