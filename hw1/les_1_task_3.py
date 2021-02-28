# Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
import random
# a. случайное целое число,
int_start = int(input('Укажите нижнюю границу случайного числа\n'))
int_stop = int(input('Укажите верхнюю границу случайного числа\n'))
int_number = random.randint(int_start,int_stop)
print(f'Полученное случайное число - {int_number}')

# b. случайное вещественное число,
float_start = float(input('Укажите нижнюю границу случайного числа\n'))
float_stop = float(input('Укажите верхнюю границу случайного числа\n'))
float_number = random.uniform(float_start,float_stop)
print(f'Полученное случайное число - {float_number}')
# c. случайный символ.
from random import random
length_start = ord(input('Укажите первый случайный символ алфавита '))
length_stop = ord(input('Укажите последний случайный символ алфавита '))

print(chr(int(random()*(length_start-length_stop))+length_start+1))
