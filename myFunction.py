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

# x = [1, 2, 4]
# funcs = [add, mul]
# for f in funcs:
#     print(calcAll(x, f))

def square(x):
    return x**2

# print(calcAll(10, square))
# print(calcAll(10, lambda x: x**2))

# 加分題
# 用匿名函式寫出：輸入 3，輸出[1, 2, 3]
# 用匿名函式寫出：輸入 4，輸出[1, 2, 3, 4]
# 用匿名函式寫出：輸入 5，輸出[1, 2, 3, 4, 5]
# a = lambda x: list(range(1, x+1))
# a = lambda x: [y for y in range(1, x+1)]
# a = lambda x: [y**2 for y in range(1, x+1)]
# print(calcAll(10, a))

# s = [(4, 7), (2, 3), (5, 1), (7, 4)]
# result1 = sorted(s, key=lambda e: e[0])
# result2 = sorted(s, key=lambda e: e[1])
# print(result1)
# print(result2)

a = 1
b = 2
c = 3
def test(x):
    global a
    a = 11
    print('函式內部的區域變數a', a)
    print('全域變數b', b)
        
test(a)
print('全域變數a', a)



