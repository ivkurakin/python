class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def set_date(cls, user_str):
        day = int(user_str.split('-')[0])
        month = int(user_str.split('-')[1])
        year = int(user_str.split('-')[2])
        return cls(day, month, year)

    @staticmethod
    def validator(self):
        if self.month < 1 or self.month > 12:
            raise ValueError
        if self.day < 1 or self.day > 31:
            raise ValueError
        if self.month == 2 and self.day > 29 and self.year % 4 == 0:
            raise ValueError
        if self.month == 2 and self.day > 28 and self.year % 4 != 0:
            raise ValueError
        if self.month == 4 and self.day > 30:
            raise ValueError
        if self.month == 6 and self.day > 30:
            raise ValueError
        if self.month == 9 and self.day > 30:
            raise ValueError
        if self.month == 11 and self.day > 30:
            raise ValueError


try:
    date_str = '28-02-2021'
    Date.validator(Date.set_date(date_str))
except ValueError:
    print('Неверно введена дата')
else:
    print(f'Дата введена верно')
