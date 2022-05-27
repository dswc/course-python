# -*- coding: utf-8 -*-

# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'d': 4, 'e': 5, 'f': 6}
# dict1.update(dict2)
# dict3 = {**dict1, **dict2}

def prnPriceOri(name, color1, color2, color3):
    print(f'{name},', color1, color2, color3)

def prnPrice(name, **kwargs):
    print(f'{name},', kwargs)

prnPrice('chris', red=3, green=7, blue=7)

dict4 = {'red': 3, 'green': 7, 'blue': 7}
prnPrice('chris', dict4)
prnPrice('chris', **dict4)

