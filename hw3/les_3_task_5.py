# в массиве найти максимальный
# отрицательный элемент. Вывести
# на экран его значение и позицию в массиве.
import random
length = int(input('Укажите длину массива '))
my_list = [random.randint(-99,99) for _ in (range(length))]
min_index = 0
print('Полученный массив:',*my_list)

for i in my_list:
    if my_list[min_index] > i:
        min_index = my_list.index(i)
if my_list[min_index] >= 0:
    print(f'В массиве нет отрицательных элементов')
else:
    print(f'В массиве минимальный отрицательный элемент \
{my_list[min_index]} \
находится в массиве на позиции {min_index+1}')



