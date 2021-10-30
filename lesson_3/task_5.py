"""Бесконечный цикл пока пользователь не введет * """


def fun_sum(val):
    rez = sum(val)
    return rez


while True:
    my_list = input('Введите числа через пробел: ').split()
    # Проверяем есть ли спец символ среди введенных
    if '*' in my_list:
        print('Выполнение завершено')
        break
    else:
        print(fun_sum(list(map(int, my_list))))

