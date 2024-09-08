class Vehicle :
    _COLOR_VARIANTS =  ['blue', 'red', 'green', 'black', 'white']
    def __init__(self,owner,_model,_color,_engine_power ):
        self.owner = owner
        self.model = _model
        self.engine_power = _engine_power
        self.color = _color

    def get_model (self):
        print( f'\033[34mМодель :{self.model}')
    def get_horsrower (self):
        print(f'\033[34mМощность :{self.engine_power}')
    def get_color (self):
       print(f'Цвет :{self.color}')
    def print_info(self):
        # print(f'{self.model}, {self.engine_power}, {self.color}, Owner :{self.owner}')
         self.get_model()
         self.get_horsrower()
         self.get_color()
         print (f'Владелец:  {self.owner}')

    def set_color (self, new_color):
        if new_color.lower() in self._COLOR_VARIANTS:
            self.color = new_color
        else:
            print(f'\033[31mНельзя сменить цвет на {new_color} ')



class Sedan(Vehicle):

     __PASSENGERS_LIMIT = 5


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

