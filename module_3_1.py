calls = 0
def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    count_calls()
    string_tuple = (len(string),string.upper(),string.lower())
    return string_tuple


def is_contains(string,list_to_search):
    string = string.upper()
    count_calls()
    is_in_list = False
    for i in list_to_search:
        if type(i) == type(string):
            i = i.upper()
            if i == string:
                is_in_list = True
                break
    return is_in_list
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)