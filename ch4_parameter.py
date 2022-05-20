def calc(w, *args):
    for arg in args:
        w = w * arg
    return w

def calc2(w, **kwargs):
    print(w, kwargs)
y = calc(3, 4, 5, 6)
print(y)
calc2('chris', a=1, b=2)
