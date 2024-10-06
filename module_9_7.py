def is_prime(func):
    def wrapper(*args,**kwargs):
        original_result = func(*args,**kwargs)
        resultTMP = 'Простое' +'\n'+str(original_result)
        if original_result > 2:
            for i in range(2,original_result):
                if original_result%i == 0:
                    resultTMP = 'Составное' +'\n'+str(original_result)
                    break
        if original_result <= 2 and original_result>0:
            resultTMP = 'Простое' + '\n' + str(original_result)
        if original_result < 0:
            resultTMP = 'Отрицательное' + '\n' + str(original_result)
        return resultTMP
    return wrapper

@is_prime
def sum_three(a,b,c):
    return a+b+c


result = sum_three(0, 0, -1)
print(result)