import time
import sys


class TrafficLight:
    __color = ""

    def check(self, cheklist):
        self.checklist = ["Красный", "Желтый", "Зеленый"]
        return self.checklist == cheklist


    def RunTraffic(self):
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

