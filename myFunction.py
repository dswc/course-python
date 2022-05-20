def add(x):
    v = 0
    for i in x:
        v += i
    return v

def mul(x):
    v = 1
    for i in x:
        v *= i
    return v

def calcAll(value, func):
    return func(value)

x = [1, 2, 4]
funcs = [add, mul]
for f in funcs:
    print(calcAll(x, f))
