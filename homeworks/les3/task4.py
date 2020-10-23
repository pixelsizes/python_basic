"""
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
"""


def my_func(x, y):
    result = x
    while y <= 0:
        result /= x
        y += 1
    return result


user_input = input('введите 2 числа действительное положительное и целое отрицательное через пробел:\n>>>')
list_input = user_input.split(' ')


if len(list_input) == 2:
    input_x = float(list_input[0])
    input_y = int(list_input[1])
    if input_x <= 0 or input_y >= 0:
        print('ошибка ввода')
    else:
        print(f'{input_x}^{input_y} = {my_func(input_x, input_y)}')
else:
    print('не 2 числа')
