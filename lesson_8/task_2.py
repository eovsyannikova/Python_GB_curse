class ZeroError(Exception):
    def __init__(self, message):
        self.message = message


try:
    data_in1 = int(input('Введете делимое: '))
    data_in2 = int(input('Введете делитель: '))
    if data_in2 == 0:
        raise ZeroError('Делить на 0 нельзя')
except ZeroError as err:
    print(err)
except ValueError:
    print("Вы ввели не число")
else:
    print(f'Результат деления {data_in1/data_in2}')

