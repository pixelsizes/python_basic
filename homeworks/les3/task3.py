"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(x, y, z):
    if x < y and x < z:
        return y + z
    if y < x and y < z:
        return x + z
    return x + y


user_input = input('введите 3 числа через пробел:\n>>>')
list_input = user_input.split(' ')
if len(list_input) == 3:
    print(f'сумма наибольших двух аргументов: {my_func(int(list_input[0]), int(list_input[1]), int(list_input[2]))}')
else:
    print('не 3 числа')
