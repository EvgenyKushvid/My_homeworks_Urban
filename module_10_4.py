import time
from queue import Queue
from threading import Thread
import random
from time import sleep


class Table:
    def __init__(self, number, guest = None):
        self.number = number
        self.guest = guest

    def __str__(self):
        return str(self.number)

class Guest (Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name


    def run (self):
        sleep(random.randint(3,8))

    def __str__(self):
        return self.name


class Cafe:
    def __init__(self, *tables):
        self.table = tables
        self.gueue = Queue()

    def busy_tables(self):
        return [table for table in tables if table.guest != None ]


    def guest_arrival(self, *guests):
        i = 0
        for guest in guests:
            for table in tables:
                if table.guest == None:
                    table.guest = guest
                    guest.start()
                    i+=1
                    print(f'{guest} сел(-а) за стол номер {table}')
                    break
                elif i >= len(tables):
                    self.gueue.put(guest)
                    print(f'{guest} в очереди')
                    break


    def discuss_guests (self):
        while not self.gueue.empty() or len (self.busy_tables()) > 0:
            for table in self.busy_tables():
                if table.guest is None or not table.guest.is_alive():
                    print(f'{table.guest} покушал(-а) и ушёл(ушла)')
                    print(f'Стол номер {table} свободен')
                    table.guest = None
                    if not self.gueue.empty():
                        table.guest = self.gueue.get()
                        print(f'{table.guest} вышел(-ла) из очереди и сел(-а) за стол номер {table}')
                        table.guest.start()




# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

