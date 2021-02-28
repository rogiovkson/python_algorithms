# Пользователь вводит две буквы. Определить, на каких местах алфавита они
# стоят и сколько между ними находится букв.
length_start = ord(input('Введите первый символ английского алфавита ').lower())
letter_number_1st = chr(length_start)
letter_number_1st = ord(letter_number_1st) - 96
length_stop = ord(input('Введите второй символ английского алфавита ').lower())
letter_number_last = chr(length_stop)
letter_number_last = ord(letter_number_last) - 96
delta = abs(letter_number_last - letter_number_1st)-1
print(f'Позиция первого символа - {letter_number_1st}, позиция второго символа - {letter_number_last}.\
\nКоличество символов между ними - {delta}')