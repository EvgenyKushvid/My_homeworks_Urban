from time import  sleep
import random
from threading import Thread, Lock

class Bank (Thread):
    lock = Lock()

    balance = 0
    def __init__(self):
        super().__init__()

    def deposit (self):
        for i in range (1, 100):
            cash = random.randint(50, 500)
            self.balance += cash
            print(f'Пополнение: {cash}, Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            sleep(0.001)

    def take (self):
        for i in range(1, 100):
            cash = random.randint(50, 500)
            print(f'Запрос на {cash}')
            if cash <= self.balance:
                self.balance -= cash
                print(f'Снятие: {cash}, Баланс:{self.balance}')
            else:
                print('Запрос отклонен, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс {bk.balance}')
