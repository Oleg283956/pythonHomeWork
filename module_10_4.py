import threading
from operator import is_not
from threading import Thread,Lock
import time
import random
import queue



guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]

number = 0


class Table:
    guest = ''
    def __init__(self,number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        pause = random.randint(3,10)
        time.sleep(pause)


class Cafe:
    q = queue.Queue()
    tables1 = []
    def __init__(self,*tables2):
        self.tables1 = tables2

    def guest_arrival(self, *guests):
        list_guests = list(guests)
        for i in list_guests:
            name_guest = i.name 
            zanjat_after_None = 0
            for j in self.tables1:
                if j.guest is None:
                    zanjat_after_None = 1
                    j.guest = name_guest
                    print(f'{name_guest} сел(-а) за стол номер {j.number}.')
                    break
            if zanjat_after_None == 0:
                print(f'{name_guest} в очереди.')
                self.q.put(name_guest)
            th = Guest(name_guest)
            th.start()
    def discuss_guests(self):
        while self.q.empty() != True:
            self.prosmotr_tables()
        if self.q.empty() == True:
            self.prosmotr_tables()
    def prosmotr_tables(self):
        for j in self.tables1:
            if j.guest is not None:
                name_of_supper = j.guest
                thprov = Guest(name_of_supper)
                if thprov.is_alive() == False:
#                    if name_of_supper != None:
                    print(f'{name_of_supper} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {j.number} свободен.')
                    if self.q.empty() == False:
                        new_name_of_supper = self.q.get()
                        j.guest = new_name_of_supper
                        print(f'{new_name_of_supper} вышел(-ла) из очереди и сел(-а) за стол номер {j.number}')
                    else:
                        j.guest = None


tables = [Table(number) for number in range(1, 6)]
guests = [Guest(name) for name in guests_names]
cafe = Cafe(*tables)
cafe.guest_arrival(*guests)
cafe.discuss_guests()

