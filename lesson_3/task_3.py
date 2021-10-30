""" Реализовать функцию my_func(), которая принимает три позиционных аргумента и
 возвращает сумму наибольших двух аргументов.
"""


def my_func(val1, val2, val3):
    arg_array = [val1, val2, val3]
    try:
        arg_array.remove(min(arg_array))
        arg_sum = sum(arg_array)
        return arg_sum

    except TypeError:
        print('Неккоректные данные')


print(my_func(1, 5, 7))
