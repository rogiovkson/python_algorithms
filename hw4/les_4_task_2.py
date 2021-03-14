import cProfile
import math
#Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное
# и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
#решето Эратосфена
n = 100000
def sieve(n):
    np1 = n + 1
    s = list(range(np1))
    s[1] = 0
    for i in range(2, int(math.sqrt(n) + 1)):
        if s[i]:
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return filter(None, s)
a = (sieve(n))
print(*a)
#70 function calls in 0.009 seconds
#простой способ проверки
b = []
def test(n):
    sieve = [i for i in range(n)]
    sieve[1] = 0

    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i

    res = [i for i in sieve if i != 0]
    b.append(res)
test(n)
print(*(b))
#7 function calls in 0.044 seconds
cProfile.run('sieve(n)')

#Решето Эратосфена - 0.009 сек
#Простой способ проверки - 0.044 сек