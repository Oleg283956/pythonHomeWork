first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(z[0]) - len(z[1])  for z in zip(first,second) if len(z[0]) != len(z[1]) )
print(list(first_result))
second_result = (len(first[i]) == len(second[j]) for i in range(0,len(first)) for j in range(0,len(second)) if i == j)
print(list(second_result))