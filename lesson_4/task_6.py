from itertools import count, cycle
# ytj,[j
# Часть 1  итератор, генерирующий целые числа, начиная с указанного

el_count = int(input('Введите число, с которого необходимо начать отсчет(число должно быть меньше 15): '))
my_list = []
# Добавлен шаг 3
for el in count(el_count, 3):
    if el > 15:
        break
    else:
        my_list.append(el)
        print(el)


# Часть 2  итератор, генерирующий целые числа, начиная с указанного
i = 0
for el in cycle(my_list):
    if i > 5:
        break
    print(el)
    i += 1
