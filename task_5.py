class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки {self.title} ручкой')


class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки {self.title} карандашом')


class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Запуск отрисовки {self.title} маркером')


stat = Stationery('"Родительский класс"')
stat.draw()
pen = Pen('"Класс Pen"')
pen.draw()
pencil = Pencil('"Класс Pencil"')
pencil.draw()
handle = Handle('"Класс Handle"')
handle.draw()
