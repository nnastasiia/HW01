class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '.': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2020 >= year >= 0:
                    return f'ok'
                else:
                    return f'year not valid'
            else:
                return f'month not valid'
        else:
            return f'day not valid'

    def __str__(self):
        return f'now {Data.extract(self.day_month_year)}'


today = Data('20 . 03 . 2020')
print(today)
print(today.valid(11, 13, 2011))
print(Data.extract('01 . 01 . 2001'))
print(today.extract('13 . 03 . 3000'))
print(Data.valid(6, 1, 2000))