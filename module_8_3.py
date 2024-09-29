class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message =  message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message =  message

class Car:

    def __init__(self, model, _vin, _numbers):
        self.model = model
        if self._is_valid_vin(_vin):
            self._vin = _vin
        if self.__is_valid_numbers(_numbers):
            self._numbers = _numbers

    def _is_valid_vin(self, vin_number):
            if not isinstance(vin_number, int):
                raise IncorrectVinNumber('Некоректный тип vin номерa')
            elif not vin_number >= 1000000 and vin_number <= 9999999:
                raise IncorrectVinNumber('Неверный диапазон для vin номера')
            else:
                return True
    def __is_valid_numbers (self, numbers):
            if not isinstance(numbers, str):
                raise IncorrectCarNumbers('Некоректный тип данных для номеров')
            elif not len(numbers) == 6 :
                raise  IncorrectCarNumbers('Неверная длинна номера')
            else:
                return True


try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')