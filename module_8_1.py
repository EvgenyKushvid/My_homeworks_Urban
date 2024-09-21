
def out_format(*text):
    print("\033[3m -\033[31m{}".format(text))

def add_everything_up(a,b):
    try:
        result = a + b
    except ( TypeError) as exc:
        out_format(f'{a},{b}  Ошибка - {exc},{exc.args}')
        return a,b
    else:
        return result


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

