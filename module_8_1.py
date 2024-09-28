def add_everything_up(a,b):
    try:
        res = a + b
    except TypeError:
        if  not isinstance(a,str):
            a = str(a)
        if  not isinstance(b,str):
            b = str(b)
        res = a + b
    else:
        res = a + b
        if isinstance(res,float):
            res = round(res,3)
    finally:
        return res

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456,7))
