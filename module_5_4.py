class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args)
        return object.__new__(cls)

    def __init__(self, name, number_of_floor):
        self.name = name
        self.number_of_floor = number_of_floor

    def go_to (self, new_floor):
        for i in range(1, new_floor+1):
            if  new_floor > self.number_of_floor:
                print("Такого этажа не существует")
                break
            else:
                print(i)
    def __del__(self):
        print(f'{self.name} снесен, но остается в истории')
    def __len__(self):
        return self.number_of_floor

    def __str__(self):
        return f"Название {self.name} . к-во этажей {self.number_of_floor}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floor == other.number_of_floor

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floor < other.number_of_floor

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floor > other.number_of_floor



    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floor <= other.number_of_floor


    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floor >= other.number_of_floor


    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floor != other.number_of_floor



    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floor += value
            return self


    def __radd__(self, value):
        if isinstance(value, int):
            return self.__add__(value)


    def __iadd__(self, value):
        if isinstance(value, int):
            return self.__add__(value)





h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)