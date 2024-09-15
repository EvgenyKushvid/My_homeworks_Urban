from pprint import pprint

class Product:
    def __init__(self, name,weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__ (self):
        return f'{self.name} , {self.weight} , {self.category}'

class Shop:
    _file_name = '../dop/product.txt'

    def get_products (self):
        file = open(self._file_name, 'r')
        data = file.read()
        file.close()
        return data

    def add (self, *product):
        file = open(self._file_name, 'a')
        for prod in product:
            if prod.name not in self.get_products():
                file.write(prod.__str__())
                file.write('\n')
            else:
                print(f'Продукт {prod.name} уже есть в магазине')
        file.close()



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
