class ValueNotInt(Exception):
    def __init__(self, message):
        self.message = message


input_val = []
i = ""
while True:
    i = input('Введите значение: ')
    if i == 'stop':
        print('Ввод данных завершен')
        break
    try:
        if i.isdigit():
            input_val.append(int(i))
        else:
            raise ValueNotInt('Вы ввели не число, повторите ввод')
    except ValueNotInt as err:
        print(err)
        continue
print(f'Введеный список:\n{input_val}')
