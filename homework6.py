my_dict = {"Vasya": 1975, 'Egor':1999, "Masha":2002}
print("Dict ",my_dict)
print("Existing value",my_dict["Masha"])
print("Not existind value", my_dict.get("Denis"))
my_dict.update ({'Kamila': 1981,"Artem":1915 })
print(my_dict.get('Egor'))
del my_dict['Egor']
print('Modified dictionary ',my_dict)
my_set = {1,"Apple", 42.34,1 ,4}

print('Set ',my_set)
my_set.update([77, "Snow",(5,6,9)])
my_set.remove(1)
print('Modified set ',my_set)