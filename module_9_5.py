class StepValueError(ValueError):
    pass

class Iterator:
    ar1 = []
    start = 0
    stop = 0
    step = 0
    pointer = 0
    def __new__(cls, *args, **kwargs):
        list_args = list(args)
        cls.start = list_args[0]
        cls.stop = list_args[1]
        if len(list_args) == 2:
            list_args.append(1)
            cls.step = 1
            '''
            if cls.stop > cls.start:
                list_args.append(1)
                cls.step = 1
            if cls.start > cls.stop:
                list_args.append(-1)
                cls.step = -1
            '''
        else:
            cls.step = list_args[2]
        if list_args[2] == 0:
            raise StepValueError()
        cls.pointer = list_args[0] - cls.step
        cls.ar1 = list_args
        return super().__new__(cls)


    def __init__(self,*args):
        self.args = tuple(self.ar1)
        pass

    def __iter__(self,*args):
        list_args = list(self.args)
        self.start = list_args[0]
        self.stop = list_args[1]
        self.step = list_args[2]
        self.pointer = list_args[0] - list_args[2]
        return self

    def __next__(self):
        self.pointer += self.step
        if self.step > 0:
            if self.pointer <= self.stop:
                return self.pointer
            else:
                raise StopIteration
        if self.step < 0:
            if self.pointer >= self.stop:
                return self.pointer
            else:
                raise StopIteration


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')
iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)
for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()
