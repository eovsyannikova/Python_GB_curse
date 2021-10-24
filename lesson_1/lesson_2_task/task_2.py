input_list = []
output_list = []
elements_counter = int(input('Введите количество элементов для списка: '))

for i in range(elements_counter):
    # запрашиваем значение у пользователя
    element = input(f"Введите значение для первого списка {i + 1}-е: ")
    # добавляем элемент в список
    input_list.append(element)
# Выводим первый список
print(input_list)

input_list_len = len(input_list)

# вариант решения  1
for i in range(0, input_list_len, 2):
    if i < input_list_len - 1:
        next_index = i + 1
        output_list.insert(i, input_list[next_index])
        output_list.insert(next_index, input_list[i])
    else:
        # такая ситуация возможна только при нечетной длине списка
        output_list.append(input_list[-1])
# Выводим итоговый список
print(output_list)

# вариант решения 2
# if input_list_len % 2 == 0:
#     for i in range(0, input_list_len, 2):
#         next_index = i + 1
#         output_list.insert(i, input_list[next_index])
#         output_list.insert(next_index, input_list[i])
# else:
#     for i in range(0, input_list_len - 1, 2):
#         next_index = i + 1
#         output_list.insert(i, input_list[next_index])
#         output_list.insert(next_index, input_list[i])
#     # Добавляем нечетный элемент в конец списка
#     output_list.append(input_list[-1])
# Выводим итоговый список
# print(output_list)
