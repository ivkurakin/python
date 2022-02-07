class Worker:

    def __init__(self, name, surname, wage, bonus, position=None):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def __init__(self, name, surname, wage, bonus):
        super().__init__(name, surname, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


user_pos = Position('Иван', 'Иванов', 50000, 5000)
print(user_pos.get_full_name(), user_pos.get_total_income())
