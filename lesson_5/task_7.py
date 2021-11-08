import os
import json

path = os.path.join(os.getcwd(), "task_7.txt")
path_json = os.path.join(os.getcwd(), "task_7.json")
print(path)
firm_dict = {}
average_dict = {}
firm_list = []
data_json = ""
try:
    with open(path, "r", encoding='utf-8') as file_in:
        print('Файл открыт для четния')
        for line in file_in.readlines():
            # Разбираем строку в переменные
            key, form, proceeds, cost = line.split()
            # Рассчет прибыли
            profit = float(proceeds) - float(cost)
            # Добалвяем в словарь только фирмы с прибылью
            if profit > 0:
                firm_dict[key] = profit
        # формируем словарь со средней прибылью
        average_dict['average_profit'] = sum(val for val in firm_dict.values()) / len(firm_dict)
    # Формируем итоговый список
    firm_list = [firm_dict, average_dict]
    print(f"Итоговый список для обработки JSON: {firm_list}")

    # Создаем файл JSON и записываем в него список
    with open(path_json, 'w', encoding='utf-8') as file_out:
        json.dump(firm_list, file_out)
        print('Файл записан в формате json')
    # Читаем файл JSON
    with open(path_json, 'r', encoding='utf-8') as file_out:
        data_json = json.load(file_out)
        print(f'Данные файле task_7.json записаны в следующем виде {data_json}')

except IOError:
    print("Произошла ошибка ввода-вывода!")
