class Clothes:
    def __init__(self, v, h, type_cl):
        self.v = v
        self.h = h
        self.count = type_cl

    @property
    def count(self):
        return f"Необходимо {self.__count} ткани"

    @count.setter
    def count(self, type_cl):
        if type_cl == "Пальто":
            self.__count = self.v / 6.5 + 0.5
        elif type_cl == "Kостюм":
            self.__count = 2 * self.h + 0.3
        else:
            None


a = Clothes(45, 30, "Пальто")

print(a.count)



#
#
#
