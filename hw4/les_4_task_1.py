# Проанализировать скорость и сложность одного любого
# алгоритма из разработанных в рамках домашнего
# задания первых трех уроков.
import cProfile

import random

# в массиве найти максимальный
# отрицательный элемент. Вывести
# на экран его значение и позицию в массиве.
#быстрая сортировка (Хоара)
length = int(1000)
my_list = [random.randint(-99, 99) for _ in (range(length))]
print(f'Полученный массив: {my_list[:20]}...{my_list[979:]}')
def quicksort(my_list):
    if len(my_list) <= 1:
        return my_list
    else:
        q = random.choice(my_list)
        l_my_list = [n for n in my_list if n < q]
        e_my_list = [q] * my_list.count(q)

        b_my_list= [n for n in my_list if n > q]

    return quicksort(l_my_list) + e_my_list + quicksort(b_my_list)
min_number = quicksort(my_list)
#2398 function calls (2014 primitive calls) in 0.002 seconds
print(f'Отсортированный массив методом Хоара: {min_number[:20]}...{min_number[979:]}\
\nМаксимальное отрицательное число: {min_number[0]}')

#Сортировка пузырьком

def bubble_sort(my_list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(my_list) - 1):
            if my_list[i] > my_list[i + 1]:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
                swapped = True
bubble_sort(my_list)
#930 function calls in 0.149 seconds
print(f'Отсортированный массив методом Пузырька:{my_list[:20]}...{my_list[979:]}\
\nМаксимальное отрицательное число: {my_list[0]}')




#сортировка слиянием
def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:

            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1

            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1


        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1

        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list

def merge_sort(my_list):
    if len(my_list) <= 1:
        return my_list
    mid = len(my_list) // 2

    # Сортируем и объединяем подсписки
    left_list = merge_sort(my_list[:mid])
    right_list = merge_sort(my_list[mid:])

    return merge(left_list, right_list)
#17973 function calls (15975 primitive calls) in 0.007 seconds
merge_sorted = merge_sort(my_list)
print(f'Отсортированный массив методом Слияния:{merge_sorted[:20]}...{merge_sorted[979:]}')
print('Максимальный отрицательный элемент: ', merge_sorted[0])

cProfile.run('bubble_sort(my_list)')


#Сортировка пузырьком - 0,149 сек
#Сортировка слиянием - 0,007 сек
#Сортировка Хоара - 0,002 сек