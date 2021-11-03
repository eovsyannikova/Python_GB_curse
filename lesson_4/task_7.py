import math


def fact(val):
    for i in range(1, val + 1):
        yield i


n = int(input('Введите число для расчета факториала: '))
rez = 1

for el in fact(n):
    rez *= el

print(f"Факториал числа {n}: {rez}")
# для проверки результата сравнение с функцией из библиотеки math
print(f"Факториал числа, рассчитанный с помощью math {math.factorial(n)}")

