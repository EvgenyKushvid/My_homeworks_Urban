
import math

class Figure:
    sides_count = 0
    filled = False

    def __init__(self, color, *sides):
        self._color = color
        _sides = []
        if len(sides) == self.sides_count:
            for i in range(self.sides_count):
                _sides.append(sides[i])
        else:
            for i in range(self.sides_count):
                _sides.append(1)
                i += 1
        self._sides = _sides



    def get_color(self):
        return list(self._color)

    def __is_valid_color(self, r, g, b):
        if type(r) == int and 0 <= r <= 255 and \
                type(g) == int and 0 <= g <= 255 and \
                type(b) == int and 0 <= b <= 255:
            return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self._color = (r, g, b)
        return self._color
    def get_sides(self):
        return list(self._sides)

    def __is_valid_sides(self, *sides):
        _sides = []
        for side in sides:
            if type(side) == int and side > 0:
                _sides.append(side)
        if len(_sides) == self.sides_count:
            return True

    def set_sides(self, *new_sides):
       if self.__is_valid_sides(*new_sides):
            self._sides = new_sides

class Circle(Figure):
    sides_count = 1
    filled = False

    def __len__(self):
        return  self._sides[0]

    def __radius (self):
        return self._sides[0] / math.pi *2

    def  get_square (self):
        print(f'Радиус круга {self.__radius()}')
        return  3.14 * self.__radius()**2



class Triangle(Figure):
    sides_count = 3
    filled = False

    def get_square (self):
        sides = self.get_sides()
        p = 0.5 * sum(sides)
        sguare = math.sqrt(p * (p-sides[0]) * (p-sides[1])* (p-sides[2])    )
        #print(f'Полупериметр = {p}, Площадь треугольника  {sguare}')
        return  round(sguare,2)

class Cube(Figure):
    sides_count = 12
    filled = False

    def __init__(self,color,*sides):
        super().__init__(color,*sides)
        #self._color = color
        _sides = []
        if len(sides) == 1:
            for i in range(self.sides_count):
                _sides.append(sides[0])
        else:
            for i in range(self.sides_count):
                _sides.append(1)
                i += 1
        self._sides = _sides


    def get_volume(self):
            return self._sides[0] ** 3





circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

# Дальше все мое
print("---------- Мои проверки --------------")
tr1 = Triangle((45,46,47), 6,14,19)
tr2 = Triangle((45,46,47), 6,14,19, 23)
cube2 =  Cube((200, 200, 100), 9, 12)
circle2 = Circle((200, 200, 100), 10, 15, 6)
print(circle2.get_sides())
print(tr2.get_sides())
print(cube2.get_sides())
print(tr1.get_sides())
print(circle1.get_square())
print(cube1.get_volume())
print(tr1.get_square())