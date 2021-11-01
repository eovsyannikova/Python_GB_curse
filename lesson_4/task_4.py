item_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
rez_list = [item for item in item_list if item_list.count(item) == 1]
print(rez_list)