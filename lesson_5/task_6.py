import os

path = os.path.join(os.getcwd(), "task_6.txt")
print(path)
lesson_dict = {}
try:
    with open(path, "r", encoding='utf-8') as file_in:
        print('Файл открыт для чтения')
        # Перебираем строки
        for line in file_in.readlines():
            # Разделяем ключи и значение
            key, value = line.split(':')
            # формируем список из значений по срезам и считаем сумму
            sum_val = sum([int(val[:val.find("(")]) for val in value.split()])
            # Составляем словарь
            lesson_dict[key] = sum_val
        print(lesson_dict)

except IOError:
    print("Произошла ошибка ввода-вывода!")