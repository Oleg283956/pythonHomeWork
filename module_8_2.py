def personal_sum(numbers):
    list_typleRes = []
    result = 0
    incorrect_data = 0
    list_numbers = list(numbers)
    for i in list_numbers:
        try:
            result += i
        except TypeError:
            if not isinstance(i,int) and not isinstance(i,float) and not isinstance(i,complex):
                print(f'Некорректный тип данных для подсчёта суммы - {i}')
                incorrect_data += 1
    list_typleRes.append(result)
    list_typleRes.append(incorrect_data)
    return tuple(list_typleRes)

def calculate_average(numbers):
    result = 0
    nocorr_numbers = 0
    try:
        l_numb = list(numbers)
    except TypeError:
        print('В numbers записан некорректный тип данных.')
        result = None
        nocorr_numbers =1
    if nocorr_numbers == 0:
        l_res = list(personal_sum(numbers))
        summ_numb = l_res[0]
        count_numb = len(list(numbers)) - l_res[1]
        try:
            result = summ_numb / count_numb
        except ZeroDivisionError:
            result = 0
    return result

print(f'Результат 1: {calculate_average('1, 2, 3')}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать

