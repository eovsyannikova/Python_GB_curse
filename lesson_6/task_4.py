from random import randint


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        if self.is_police:
            return f"Машина полиции начала патрулирование"
        else:
            return f"{self.color} {self.name} начала движение"

    def stop(self):
        return f"остановилась"

    def turn(self, direction):
        return f"повернула {direction}"

    def show_speed(self):
        return f"текущая скорость - {self.speed}"


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            high_speed = "скорость превышена!"
            return f"{self.color} {self.name} текущая скорость - {self.speed} {high_speed} "
        else:
            return f"{self.color} {self.name} текущая скорость - {self.speed}"


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            high_speed = "скорость превышена!"
            return f"{self.color} {self.name} текущая скорость - {self.speed} {high_speed} "
        else:
            return f"{self.color} {self.name} текущая скорость - {self.speed}"


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


speed = randint(1, 220)
s = SportCar(speed, 'Красная', 'Ferrari')
print(s.go(), s.show_speed(), s.turn('налево'), s.stop(), sep='\n', end='\n ====== \n')

t = TownCar(speed, 'Желтая', 'Киа')
print(t.go(), t.show_speed(), t.turn('на парковку'), t.stop(), sep='\n', end='\n ====== \n')

w = WorkCar(speed, 'Белая', 'Вольво')
print(w.go(), w.show_speed(), w.turn('к работе'), w.stop(), sep='\n', end='\n ====== \n')

p = PoliceCar(speed, 'Синяя', 'Тойота Полиции')
print(p.go(), p.show_speed(), p.turn('к нарушителю'), p.stop(), sep='\n', end='\n ====== \n')
