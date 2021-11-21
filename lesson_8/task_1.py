class Date:
    @classmethod
    def to_extract(cls, date_in):
        dd, mm, yy = map(int, date_in.split('-'))
        return f'День - {dd}, Месяц - {mm}, Год - {yy}'

    @staticmethod
    def date_is_valid(date_in):
        dd, mm, yy = map(int, date_in.split('-'))
        rez_valid = (False, True)[0 < mm < 13 and 0 < yy < 2999]
        return rez_valid


print(Date.to_extract('25-09-2012'))
print(Date.date_is_valid('31-15-2012'))
