numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes =[]
not_primes =[]
is_prime = True

for num in numbers:
    if num == 1 :
        continue
    for i in range(2,num):
        is_prime = True
        if num % i == 0:
            is_prime = False
            break
    if is_prime == False:
            not_primes.append(num)
    elif is_prime == True:
        primes.append(num)
print('Primes ', primes )
print('Not primes',not_primes)