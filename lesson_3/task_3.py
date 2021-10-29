""" Реализовать функцию my_func(), которая принимает три позиционных аргумента и
 возвращает сумму наибольших двух аргументов.
"""
def my_func(val1, val2, val3):
    a = [val1, val2, val3]
    try:
        # Только если 3 значения
        a.remove(min(a))
        a_sum = sum(a)
        return a_sum

    except TypeError:
        print('Неккоректные данные')


print(my_func(1, 5, 7))
