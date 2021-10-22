number = input('Введите целое положительное число: ')
if (int(number) > 0):
    max_number = 0
    i = 0
    while i < len(number):
        if max_number < int(number[i]):
            max_number = int(number[i]);
        i += 1
    print(max_number)
else:
    print('Вы ввели не положительное число или 0')
