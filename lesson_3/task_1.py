def del_arg(first, second):
    """Деление аргументов друг на друга"""
    # Вариант 1
    # val = first / second if second != 0 else print('Делить на 0 нельзя!')
    # return val
    try:
        return first / second
    except ZeroDivisionError:
        print('Деление на 0')
        return


a = del_arg(int(input('Введите первое значение: ')), int(input('Введите второе значение: ')))
print(f"Результат деления {a}")
