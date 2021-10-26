''' Сформировать данный список
[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
'''

# Часть 1 формируем данные для исходного списка
product_list = []
product_dict = {}
keys = ['название', 'цена', 'количество', 'ед.изм']
temp_list = []
return_list = []
product_count = int(input('Введите количество '))
# number = (i for i in range(product_count))
# Цикл количества продуктов
for i in range(product_count):
    # заполняем val
    val = [input(f"Введиете {keys[x]}: ") for x in range(len(keys))]
    # формируем кортеж
    temp_list = [i + 1, (dict(zip(keys, val)))]
    product_tuple = tuple(temp_list)
    # формируем итоговый список
    product_list.append(product_tuple)
print(f"Получивший список:\n{product_list}")
''' Нужно собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например, название. 
Тогда значение — список значений-характеристик, например, список названий товаров.

Пример:
{
    “название”: [“компьютер”, “принтер”, “сканер”],
    “цена”: [20000, 6000, 2000],
    “количество”: [5, 2, 7],
    “ед”: [“шт.”]
}
'''
return_dict = {}
for key in keys:
    return_list = [v[key] for list_i in product_list for v in list_i if type(v) is dict]
    return_dict[key] = return_list
print(return_dict)
