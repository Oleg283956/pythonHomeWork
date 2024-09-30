class Car:
    model = ''
    __vin = 0
    __numbers = ''

    def __init__(self,*args,**kwargs):
        list_args = list(args)
        model = list_args[0]
        self.model = model
        self.__is_valid_vin(list_args[1])
        self.__is_valid_numbers(list_args[2])

    def __is_valid_vin(self,vin_number):
        res1 = 0
        res2 = 0
        if not isinstance(vin_number,int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        else:
            res1 = 1
        if not(vin_number >= 1000000 and vin_number <= 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            res2 = 1
        if res1 * res2 == 1:
            self.__vin = vin_number

    def  __is_valid_numbers(self,numbers):
        res1 = 0
        res2 = 0
        if not isinstance(numbers,str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        else:
            res1 = 1
        if not(len(numbers) == 6):
            raise IncorrectCarNumbers('Неверная длина номера')
        else:
            res2 = 1
        if res1 * res2 == 1:
            self.__numbers = numbers



class IncorrectVinNumber(Exception):
    def __init__(self,message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self,message):
        self.message = message



try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')