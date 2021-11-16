class Cell:
    def __init__(self, nucleus):
        self.nucleus = nucleus

    def __add__(self, other):
        return f"Результат сложения клеток - общая клетка с {self.nucleus + other.nucleus} яч."

    def __sub__(self, other):
        if self.nucleus > other.nucleus:
            return f"Результат вычитания клеток  - {self.nucleus - other.nucleus} яч."
        else:
            return f"Вычитание клеток невозможно"

    def __mul__(self, other):
        return f"Результат сложения клеток - общая клетка с {self.nucleus * other.nucleus} яч."

    def __truediv__(self, other):
        try:
            return f"Результат сложения клеток - общая клетка с {self.nucleus // other.nucleus} яч."
        except ZeroDivisionError:
            return f"Деление на 0"

    def make_order(self, count):
        rez = ""
        rem = self.nucleus
        for r in range(rem):
            if (r + 1) % count == 0:
                rez += "*/n"
            else:
                rez += "*"
        print(rez)


a = Cell(18)
b = Cell(15)

print(a.make_order(4))