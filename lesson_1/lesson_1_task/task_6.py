rez_a = float(input('Начинаем тренировку! Введите результат за первый день в км: '))
rez_b = float(input('Введите результат, к которому стремитесь: '))
force_rez = rez_a
day_z = 1
print (f"{day_z}-й день: {force_rez:.2f}")
while force_rez < rez_b:
    force_rez += force_rez * 0.1
    day_z += 1
    print (f"{day_z}-й день: {force_rez:.2f} км")
print(f"Поздравляю вы достигните результата на {day_z}-й день")