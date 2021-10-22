a = 5
b = 5.89
c = 'Практическое задание 1 "Проба пера", переменные следующего типа'
print(c, a,type(a), b, type (b))
print('<=========>')
name_user = input('Введите свое имя: ')
year = int(input('Введите год Вашего рождения в формате YYYY:'))
year_fight = 1709
years_delay = year - year_fight
print(f"{name_user}, Вы родились через {years_delay//100} века или {years_delay} лет после Полтавской битвы")