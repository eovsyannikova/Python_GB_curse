import time
import sys


class TrafficLight:
    __color = ""
    __checklist = ["Красный", "Желтый", "Зеленый"]

    def check(self, cheklist):
        return TrafficLight.__checklist == cheklist

    def RunTraffic(self):
        # Создаем список контроля цветов
        checklist = []
        __color = "Красный"
        checklist.append(__color)
        print(__color)
        time.sleep(7)
        __color = "Желтый"
        checklist.append(__color)
        print(__color)
        time.sleep(2)
        __color = "Зеленый"
        checklist.append(__color)
        print(__color)
        time.sleep(5)
        # Возвращаем список выведенных цветов светофора
        return checklist


a = TrafficLight()
try:
    while True:
        if a.check(a.RunTraffic()):
            next
        else:
            print("Ошибка порядка")
            break
except KeyboardInterrupt:
    print("Программа остановлена!")
