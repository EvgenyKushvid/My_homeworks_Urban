def print_params (a = 1, b = 'string', c = True):
    print(a,b,c)


values_list = [2,True, 'Vasia']
values_list_2 = [54.32, 'Строка' ]
values_dict = { 'a':8, 'b':'Dmitry', 'c' : False}


print_params(*values_list_2, 42)
print_params(*values_list)
print_params(**values_dict)


print_params()
print_params(b = 25)
print_params(c= [1, 2, 3])