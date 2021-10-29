"""Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия,
год рождения,город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Осуществить вывод данных о пользователе одной строкой."""

def user_param(first_name, last_name, **kwargs):
    """Обработка данных пользователя в словаре"""
    personal_dict = {}
    text = ""
    personal_dict['first_name'] = first_name
    personal_dict['last_name'] = last_name
    for param, val in kwargs.items():
        personal_dict[param] = val

    for key, value in personal_dict.items():
        text += "{0} - {1}; ".format(key, value)
    return text


a = user_param(
    # Обязательные именнованные параметры
    first_name=str(input('Введите имя: ')),
    last_name=str(input('Введите фамилию: ')),
    # Необязательные именнованные параметры
    year=(int(input('Введите год: '))),
    city=str(input('Введите город: ')),
    email=str(input('Введите email: ')),
    phone=str(input('Введите номер: ')))

print(a)