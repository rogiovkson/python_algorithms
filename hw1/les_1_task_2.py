#По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b, проходящей через эти точки.

x1 = int(input('Введите кординаты (x1): '))
y1 = int(input('Введите кординаты (y1): '))
x2 = int(input('Введите кординаты (x2): '))
y2 = int(input('Введите кординаты (y2): '))

k = (y2 - y1) / (x2 - x1)
b = y1 - k * x1
print(f'y = {k}x + {b}')