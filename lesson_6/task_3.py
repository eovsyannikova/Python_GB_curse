class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        self.full_name = f"Имя сотрудника  - {self.name} {self.surname}, Должность - {self.position}"
        return self.full_name

    def get_total_income(self):
        self.total_income = f"Суммарный доход - {self._income['wage'] + self._income['bonus']}"
        return self.total_income


name = input("Введите имя: ")
surname = input("Введите фамилию: ")
position = input("Введите должность: ")
wage = int(input("Введите оклад: "))
bonus = int(input("Введите премию: "))

person = Position(name, surname, position, wage, bonus)
print(person.get_full_name())
print(person.get_total_income())
