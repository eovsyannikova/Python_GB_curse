class Store:
    """Класс склад"""

    def __init__(self):
        self.store_dict = {'printer': [],
                           'scanner': [],
                           'xerox': []}
        self.count_all = 0

    def add_technic(self, technic):  # Добавление техники на склад
        self.store_dict[technic.flag].append(technic.parse())
        self.count_all += technic.count

    def __str__(self):
        print('Каталог магазина:')
        for x in self.store_dict:
            print(x)
            for y in self.store_dict[x]:
                print(y)
        return f'Общее количество техники на складе - {self.count_all}'

    def start(self):
        out_technic = None
        while True:
            in_flag = input('Введите тип техники 1 - принтер, 2 - сканнер, 3 -ксерокс. '
                            'Введите "stop", чтобы прекратить ввод: ')
            if in_flag == 'stop':
                break
            else:
                try:
                    if in_flag.isdigit():
                        if 0 < int(in_flag) < 4:
                            in_name = input('Введите название производителя: ')
                            in_model = input('Введите модель: ')
                            in_count = int(input('Введите количество: '))
                            if int(in_flag) == 1:
                                in_color = input('Введите тип печати: ')
                                out_technic = Printer(in_color, in_name, in_model, in_count, 'printer')
                            elif int(in_flag) == 2:
                                in_resolution = input('Введите разрешение: ')
                                out_technic = Scanner(in_resolution, in_name, in_model, in_count, 'scanner')
                            elif int(in_flag) == 3:
                                in_speed = input('Введите скорость: ')
                                out_technic = Xerox(in_speed, in_name, in_model, in_count, 'xerox')
                        else:
                            print(f'Тип техники {in_flag} не найден')
                            continue
                    else:
                        raise ValueNotInt('Данный тип техники не найден')
                except ValueNotInt as e:
                    print(e)
                    continue
                except ValueError:
                    print('Количество введено некорректно')
                    continue
                self.add_technic(out_technic)


class Technic:
    """Родительский класс оргтехника"""

    def __init__(self, name, model, count, flag):
        self.name = name
        self.count = count
        self.model = model
        self.flag = flag

    def parse(self):
        return self.name, self.count, self.model


class Printer(Technic):
    """Дочерний класс принтер"""

    def __init__(self, color, name, model, count, flag):
        self.color = color
        super().__init__(name, model, count, flag)
        self.temp_dict = {'name': self.name, 'count': self.count, 'model': self.model, 'color': self.color}

    def parse(self):
        return self.temp_dict

    def __str__(self):
        return f"Наименование продукции принтер: {self.name}, количество - {self.count}, модели - {self.model}, " \
               f"тип - {self.color}"


class Scanner(Technic):
    """Дочерний класс сканнер"""

    def __init__(self, resolution, name, model, count, flag):
        self.resolution = resolution
        super().__init__(name, model, count, flag)
        self.temp_dict = {'name': self.name, 'model': self.model, 'count': self.count, 'resolution': self.resolution}

    def parse(self):
        return self.temp_dict

    def __str__(self):
        return f"Наименование продукции сканнер: {self.name}, количество - {self.count}, модели - {self.model}, " \
               f"тип - {self.resolution}"


class Xerox(Technic):
    """Дочерний класс ксерокс"""

    def __init__(self, speed, name, model, count, flag):
        self.speed = speed
        super().__init__(name, model, count, flag)
        self.temp_dict = {'name': self.name, 'model': self.model, 'count': self.count, 'speed': self.speed}

    def parse(self):
        return self.temp_dict

    def __str__(self):
        return f"Наименование продукции ксерокс: {self.name}, количество - {self.count}, модели - {self.model}, " \
               f"скорость - {self.speed}"


class ValueNotInt(Exception):
    def __init__(self, message):
        self.message = message


s = Store()
s.start()
print(s)

# print(s)
# p_1 = Printer('ч/б', 'Panasonic', 'T300', 1, 'printer')
# p_2 = Printer('ч/б', 'Panasonic', 'T310', 3, 'printer')
# s_1 = Scanner('1200x1080', 'Sony', 'S500', 5, 'scanner')
# x_1 = Xerox('2500 об/мин', 'Xerox', 'X50', 10, 'xerox')
#
# s.add_technic(p_1)
# s.add_technic(p_2)
# s.add_technic(s_1)
# s.add_technic(x_1)
