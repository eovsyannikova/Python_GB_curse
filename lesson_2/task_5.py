my_list = [7, 5, 3, 3, 2]
user_val = int(input('Ведите место в рейтинге: '))
# Проверяем есть ли элемент в списке
if user_val in my_list:
    i = my_list.index(user_val)
    count = my_list.count(user_val)
    my_list.insert(i + count, user_val)
else:
    my_list.append(user_val)
    my_list.sort(reverse=True)

print(my_list)
