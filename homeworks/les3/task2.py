"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def element(name, surname, year, city, email, phone):
    return {'name': name, 'surname': surname, 'year': year, 'city': city, 'email': email, 'phone': phone}


list_person = []

while True:

    user_in_list = input('введите данные пользователя: \n'
                         'имя, фамилия, год рождения, город проживания, email, телефон через пробел\n>>>').split(' ')

    if len(user_in_list) != 6:
        print('неверное количество параметров попробуйте еще\n')
    else:
        list_person.append(element(user_in_list[0], user_in_list[1],
                                   user_in_list[2], user_in_list[3], user_in_list[4], user_in_list[5]))
