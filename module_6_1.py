class Animal:
    def __init__(self, name, fed = False, alive = True):
        self.name = name
        self.alive = alive
        self.fed = fed

    def __str__(self):
        return self.name
    def eat(self, food):
        if food.edible == True:
            print(f'{self.name} съел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
class Plant:
    def __init__(self, name,edible = False):
        self.edible = edible
        self.name = name
    def __str__(self):
        return self.name


class Mammal(Animal):

    pass

class Predator(Animal):
    pass

class Flower (Plant):
    pass

class Fruit (Plant):
    def __init__(self, name, edible = True):
        self.edible = edible
        self.name = name



a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')
# print('--->',p2.edible)

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
