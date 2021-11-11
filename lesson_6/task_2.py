class Road:
    __mass = 25
    __depth = 5

    def __init__(self, length=1, width=1):
        self._length = length
        self._width = width

    def calc_mass(self):
        rez = (self._length * self._width * Road.__depth * Road.__mass) / 1000
        return rez


calc_var1 = Road(20, 5000)

print(calc_var1.calc_mass())
