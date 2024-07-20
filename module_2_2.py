first = int(input("Введите первое число: "))
second  = int (input("Введите второе число:"))
third = int(input("ВВедите третье число "))

if first  == second and first== third and first == third:
    print('3. Все числа равны ', first, second, third)

elif first == second or first == third:
    print("2 числа:",first,'и', first)
elif second== first or second == third:
    print("2 числа:",second,'и',second)
else:
    print("0")