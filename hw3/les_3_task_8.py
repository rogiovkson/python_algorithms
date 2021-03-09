'''8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних
элементов строк. Программа должна вычислять сумму введенных элементов
каждой строки и записывать в последнюю ячейку строки. В конце следует
вывести полученную матрицу.'''

matrix = []

for i in range(4):
    matrix.append([])
    sum = 0
    for n in range(4):
        user_number = int(input(f'Введите {i + 1}-й элемент {n + 1}-го столбца: '))
        sum += user_number
        matrix[i].append(user_number)

    matrix[i].append(sum)
for num in matrix:
    print(('{:>2d}' * 5).format(*num))