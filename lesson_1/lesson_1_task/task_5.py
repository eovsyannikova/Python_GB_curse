
debit = float(input('Введите значение выручки: '))
credit = float(input('Введите убытки: '))
if debit > credit:
    profit = debit - credit
    print(f"Прекрасно! Вы работаете с прибылью. Ваша прибыль: {profit}")
    rent = profit / debit
    count_members = int(input('Введите количество сотрудников: '))
    vvp = profit / count_members
    print(f"Прибыль фирмы в расчете на каждого сотрудника составила: {vvp}")
else:
    print(f"Пока вы еще не начали работать с прибылью :(")