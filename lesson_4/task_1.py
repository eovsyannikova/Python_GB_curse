from sys import argv

name_script, hour, rate, bonus = argv
# param_list = [float(argv[i + 1]) for i in range(len(argv) - 1)]
# hour = param_list[0]
# rate = param_list[1]
# bonus = param_list[2]
# rez = hour * rate + bonus
print(f"Премия сотруднику составляет: {float(hour) * float(rate) + float(bonus)} ")
