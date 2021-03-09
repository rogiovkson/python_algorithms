# В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать
import random
gap = 0
length = int(input('Укажите длину массива '))
my_list = ([random.randint(-99,99) for _ in (range(length))])
mini, maxi = my_list.index(min(my_list)), my_list.index(max(my_list))
for i in my_list:
    if ((my_list.index(i) > mini and my_list.index(i) < maxi)
or (my_list.index(i) < mini and my_list.index(i) > maxi)):
        gap += i
print(f'Полученный массив - {my_list}')
print(f'Минимальное число массива: {my_list[mini]},\
 максимальное число массива: {my_list[maxi]}')
print(f'Сумма чисел между min и max числами: {gap}')