def custom_write(file_name, strings):
    strings_positions = {}
    pos = 0
    file = open(file_name, 'a', encoding='utf-8')
    for i in strings:
        pos += 1
        strings_positions[pos, str(file.tell())] = str(i)
        file.write(str(i)+'\n')
    file.close()
    return strings_positions

with open('test.txt','w'):
    pass

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)

for elem in result.items():
  print(elem)
