import threading
from threading import Thread,Lock
import time
import random


class Bank:
    balanse_Old = 0
    balance = 0
    lock = Lock()

    def __init__(self):
        pass

    def deposit(self):
        for i in range(1,101):
            self.lock.acquire()
            prihod = random.randint(50, 500)
            self.balance += prihod
            print(f'Пополнение: {prihod}. Баланс: {self.balance}')
#                if self.balance >= 500 and self.lock.locked():
#                    self.lock.release()
            if self.lock.locked():
                self.lock.release()
            time.sleep(0.001)


    def take(self):
        for i in range(1,101):
            self.lock.acquire()
            rashod = random.randint(50, 500)
            print(f'Запрос на {rashod}')
            self.balanse_Old = self.balance
            self.balance -= rashod
            if self.balance < 0:
                print('Запрос отклонён, недостаточно средств')
                self.balance = self.balanse_Old
            else:
                print(f'Снятие: {rashod}. Баланс: {self.balance}')
            if self.lock.locked():
                self.lock.release()
            time.sleep(0.001)


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

