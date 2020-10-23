"""
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def division(x, y):
    if y == 0:
        raise ArithmeticError
    return x / y


input_x = float(input('введите x\n>>>'))
input_y = float(input('введите y\n>>>'))

try:
    print(f'результат {division(input_x, input_y)}')
except ArithmeticError:
    print('ArithmeticError')
