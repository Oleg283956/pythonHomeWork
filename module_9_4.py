from random import choice

first = 'Мама мыла раму'
second = 'Рамена мало было'
result1 = list(map(lambda x, y: x == y, first, second))
print(result1)

def get_advanced_writer(file_name):
    with open(file_name,'w'):
        pass
    def write_everything(*data_set):
        list_data_set = list(data_set)
        file1 = open(file_name,'a',encoding="utf8")
        for i in list_data_set:
            file1.write(str(i)+'\n')
        file1.close()
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

class MysticBall:
    words = ()
    word = ''
    def __init__(self,*args):
        self.words = args
        self.__call__()
    def __call__(self):
        list_words = list(self.words)
        self.word = choice(list_words)
        return self.word

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
