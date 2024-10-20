from sys import modules
import inspect


def introspection_info(obj):
    allAttrAndMethods = dir(obj)
    dict = {}
    b = type(obj)
    c_t = str(b)[8:len(str(b))-2]
    dict['type'] = c_t
    try:
        attribytes = list(vars(obj))
    except:
        attribytes = []
    dict['attributes'] = attribytes
    method = []
    for i in allAttrAndMethods:
        if i not in attribytes:
            method.append(i)
    dict['methods'] = method
    module = inspect.getmodule(obj)
    mod1 = str(module)
    mod1 = mod1[9:17]
    if mod1 == '':
        mod1 = '__main__'
    dict['module'] = mod1
    return dict

class Humm:
    name = ''
    age = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def hello(self):
        print(f'Hello {self.name} !!!')

hum1 = Humm('ZZZ',111)

number_info = introspection_info(hum1)
print(number_info)

number_info = introspection_info(42)
print(number_info)

number_info = introspection_info('sss')
print(number_info)

