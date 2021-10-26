input_str = input('Введите слова через пробел: ')
# Разбираем введенные значения в список
list_str = input_str.split()
print(list_str)
# используем функцию enumerate для нумерации
for ind, el in enumerate(list_str, 1):
    # используем тернарный оператор для проверки кол-ва символов
    el = (el, el[0:10])[len(el) > 10]
    print(ind, el)