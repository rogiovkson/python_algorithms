# В массиве случайных целых
# чисел поменять местами
# минимальный и максимальный элементы.
import random
count = 0
while count != 1:
    a = int(input('Введите минимальное число диапазона массива '))
    b = int(input('Введите максимальное число диапазона массива '))
    user_range = int(input('Введите количество чисел массива '))
    count += 1
my_list = [random.randint(a,b) for _ in (range(user_range))]
mini, maxi = my_list.index(min(my_list)), my_list.index(max(my_list))
print(f'список до махинаций {my_list}')
my_list[mini], my_list[maxi] = my_list[maxi], my_list[mini]
print('список после махинаций', *my_list)