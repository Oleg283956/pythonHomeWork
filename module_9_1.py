def apply_all_func(int_list, *functions):
    result = {}
    list_functions = list(functions)
    for i in list_functions:
        nameFunct = i.__name__
        str_Zn_Funct = nameFunct+'('+str(int_list)+')'
        method = eval(str_Zn_Funct)
        result[nameFunct] = method
    return  str(result)

print(apply_all_func([6, 20, 15, 9], max, min),end=' ')
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))