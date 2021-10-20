while True:
    number=int(input('Введите число: '))
    if 0<number<10 :
        number=number**2
        print('Результат: ', number)
        break
    else:
        print('Диапазон допустимых значений от 0 до 10 (не включительно)')
