class Stationery:
    def __init__(self, title=""):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки\n'


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f"Эта {self.title} интересно геливая или шариковая!\n"


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f"Это {self.title} им можно нарисовать шарж!\n"


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)
    def draw(self):
        return f"Это {self.title} давайте выделим суть!\n"

s = Stationery()
print(s.draw())
p1 = Pen('ручка')
print(p1.draw())
p2 = Pencil('карандаш')
print(p2.draw())
h = Handle('маркер')
print(h.draw())
