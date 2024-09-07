from math import inf

def divide(x,y):
    res = 0
    if y != 0:
        res = x/y
    else:
        res = inf
    return res
