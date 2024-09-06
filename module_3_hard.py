summa = 0

def calculate_structure_sum(list_):
    global  summa
    for i in list_:
        if type(i) == str:
            summa = summa + len(i)
        if type(i) == int:
            summa = summa + i
        if type(i) == list:
            calculate_list(i)
        if type(i) == set:
            listSet =list(i)
            calculate_list(listSet)
        if type(i) == dict:
            calculate_dict(i)
        if type(i) == tuple:
            listTuple =list(i)
            calculate_list(listTuple)
    return summa



def calculate_list(sp):
    global summa
    for i in sp:
        if type(i) == set:
            listSet =list(i)
            calculate_list(listSet)
        if type(i) == int:
           summa = summa + i
        if type(i) == str:
            summa = summa + len(i)
        if type(i) == list:
            calculate_list(i)
        if type(i) == dict:
            calculate_dict(i)
        if type(i) == tuple:
            listTuple =list(i)
            calculate_list(listTuple)

def calculate_dict(dict1):
    global summa
    dict_keys = dict1.keys()
    calculate_list(dict_keys)
    dict_values = dict1.values()
    calculate_list(dict_values)


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)










































































































































