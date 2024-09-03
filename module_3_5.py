result = 1

def get_multiplied_digits(number):
    global result
    str_number = str(number)
    str_number_to_chislo = int(str_number)
    str_number = str(str_number_to_chislo)
    first = int(str_number[0:1:])
    result = first * result
    str_number = str_number[1::]
    if len(str_number) >= 1:
        get_multiplied_digits(int(str_number))
    return result

get_multiplied_digits(40203)
print(result)