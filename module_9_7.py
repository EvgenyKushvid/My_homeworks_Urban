

def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        k = 0
        for i in range(2, res // 2 + 1):
            if (res % i == 0):
                k += 1
        if (k <= 0):
            print("Простое")
        else:
            print("Сложное")
        return func(*args)
    return wrapper

@is_prime
def sum_three (*args):
    return sum ((args))


result = sum_three(2,3,6)
print(result)