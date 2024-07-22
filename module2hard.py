num = int(input("Введите число (3 - 20): "))

i = 1
result =[]
for i in range (1,20):
    for j in range(i+1,21):
        if i + j == num and (i + j)%num == 0\
            or num % (i + j) == 0:
                result.append(i)
                result.append(j)

print("Password :" ,*result)
