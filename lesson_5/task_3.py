# Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
# Выполнить подсчёт средней величины дохода сотрудников.
# Используется файл task3.txt
import os

path = (os.path.join(os.path.abspath(os.getcwd()), "task3.txt"))
personal_dict = {}
personal_list = []
average_salary = 0.0
try:
    with open(path, "r", encoding="cp1251") as file:
        print('Файл открыт в режиме чтения')
        # Читаем файл построчно
        for line in file.readlines():
            # Формируем словарь
            (key, value) = line.split()
            rate = float(value)
            personal_dict[key] = rate
            # Формируем список сотрудников с з/п выше 20к
            personal_list.append(key) if rate > 20000 else next
    # Рассчитываем среднюю зарплату
    average_salary = sum([val for val in personal_dict.values()]) / len(personal_dict.keys())

    print("Сотрудники, чей доход плата больше 20 тысяч: {}".format(", " . join(personal_list)))
    print(f"Средний доход сотрудников: {average_salary:.3f}")

except IOError:
    print("Произошла ошибка чтения файла!")

