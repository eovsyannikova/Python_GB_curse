second = int(input('Введите время в секундах: '))
hour = second // 3600
seconds_in_hour = hour * 3600
seconds_delay = second - seconds_in_hour
minute = seconds_delay // 60
second = seconds_delay - minute * 60
print(f"{hour:02}:{minute:02}:{second:02}")