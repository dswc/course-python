def printStr(name, title='未知'):
    print(f'name={name}, title={title}')

def calc(w, h):
    return (w+h)*2, w*h

printStr('chris', 'teacher')
y, z = calc(3, 4)
