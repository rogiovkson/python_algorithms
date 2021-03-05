#Написать программу, которая будет складывать, вычитать,
# умножать или делить два числа. Числа и знак операции
# вводятся пользователем. После выполнения вычисления
# программа не завершается, а запрашивает новые данные
# для вычислений. Завершение программы должно выполняться
# при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак
# (не '0', '+', '-', '', '/'), программа должна сообщать
# об ошибке и снова запрашивать знак операции.
# Также она должна сообщать пользователю о
# невозможности деления на ноль, если
# он ввел его в качестве делителя.
print('Для выхода из программы введите "0" вместо знака операции')
# class MyError(Exception):
#     def __init__(self,*args):
#          args = operation_sign
#             # print('нужно ввести только знаки деления или 0')
while True:
    operation_sign = (input('Введите знак операции. \n'))
    if operation_sign == '0':
        print('Выход из программы')
        break
    if operation_sign == '+' or operation_sign == '*' or operation_sign == '-' or operation_sign == '/':
        try:
            number1 = int(input('Введите первое число. \n'))
            number2 = int(input('Введите второе число. \n'))
            if operation_sign == '+':
                def summ(*args):
                    return number1 + number2
                print(f'сумма введенных чисел равна: {summ()}')
            elif operation_sign == '-':
                def deduction(*args):
                    return number1 - number2
                print(f'разность веденных чисел {number1} и {number2} \
равна {deduction()}')
            elif operation_sign == '*':
                def multiplier(*args):
                    return number1 * number2
                print(f'{number1} умножить на {number2} равно: {multiplier()}')
            elif operation_sign == '/' or operation_sign == ':':
                def div(*args):
                    return number1/number2
                print(f'делимое - {number1}, делитель - {number2},\
частное - {div()}')
        except ZeroDivisionError:
            print('Делить на ноль нельзя')
        except ValueError:
            print('Необходимо ввести число')
    else:
        print('Необходимо ввести знаки деления или 0')
        continue


