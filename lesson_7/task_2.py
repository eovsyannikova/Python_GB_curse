

class Clothes:
    def __init__(self, V, H, type_clothes):
        self.V = V
        self.H = H
        self.type_clothes = type_clothes

    @property
    def tissue_consumption(self):
        return round(self.__tissue, 2)

    @tissue_consumption.setter
    def type_clothes(self, type_clothes):
        if type_clothes == "Пальто":
            self.__tissue = self.V / 6.5 + 0.5
        elif type_clothes == "Kостюм":
            self.__tissue = 2 * self.H + 0.3
        else:
            self.__tissue = 0

    def tissue(self):
        return f"Необходимо {str(self.tissue_consumption)} ткани"


a = Clothes(45, 30, "Пальто")

print(a.tissue())




