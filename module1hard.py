grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_list = list(students) #преобразуем множество в список
students_list.sort() #сортируем список
new_grades=[] #содаем новый список для средних значений
for in_list in grades: # перебоо списка
    res = round(sum(in_list)/len(in_list),1) #вычисление среднего значения с округлением до 1 знака
    new_grades.append(res) # зааолняем новый список
#создаем новый объедененный и отсортированный словарь
result_list = dict(zip(students_list,new_grades))
print(result_list)