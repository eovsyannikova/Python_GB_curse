""" Хотелось попробовать использовать в функции цикл перебора входных значений"""


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


result = user_param(
    # Обязательные именнованные параметры
    first_name=input('Введите имя: '),
    last_name=input('Введите фамилию: '),
    # Необязательные именнованные параметры
    year=input('Введите год: '),
    city=input('Введите город: '),
    email=input('Введите email: '),
    phone=input('Введите номер: '))

print(result)
