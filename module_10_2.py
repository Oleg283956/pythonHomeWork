import time
from time import sleep
from threading import Thread

class Knight(Thread):
    end = 0
    name = ''
    power = 0
    enemys = 100
    count_days = 0

    def __init__(self,name,power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        if self.count_days == 0:
            print(f'{self.name}, на нас напали!')

        if self.enemys > 0:
            count_groups = round(self.enemys/self.power)
            for i in range(1,count_groups+1):
                self.count_days += 1
                self.enemys -= self.power
                print(f'{self.name} , сражается {self.count_days} день(дня), осталось {self.enemys} воинов')
                if self.enemys == 0:
                    time.sleep(1.5)
                    print(f'{self.name} одержал победу спустя {self.count_days} дней(дня)!')
                    self.end = 1
                    if first_knight.end * second_knight.end == 1:
                        print('Все битвы закончились!')
                    break
                time.sleep(1)

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

thr_1 = Thread(target=first_knight.start(),args=('Sir Lancelot', 10))
thr_2 = Thread(target=second_knight.start(),args=("Sir Galahad", 20))

thr_1.start()
thr_1.join()
thr_2.start()
thr_2.join()
