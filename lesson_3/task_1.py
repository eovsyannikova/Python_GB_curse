def del_arg(val1, val2):
    """Деление аргументов друг на друга"""
    # Вариант 1
    # val = val1 / val2 if val2 != 0 else print('Делить на 0 нельзя!)')
    # return val
    try:
        val = val1 / val2
        return val
    except ZeroDivisionError:
        print('Деление на 0')
        return


a = del_arg(int(input('Введите первое значение: ')), int(input('Введите второе значение: ')))
print(f"Результат деления {a}")
