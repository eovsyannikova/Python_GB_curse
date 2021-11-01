from sys import argv

name_script, hour, rate, bonus = argv
print(f"Премия сотруднику составляет: {float(hour) * float(rate) + float(bonus)} ")
