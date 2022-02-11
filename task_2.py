from abc import ABC, abstractmethod


class Clothes(ABC):
    sum_cloth = 0

    @property
    @abstractmethod
    def calc_cloth(self):
        pass


class Coat(Clothes):

    def __init__(self, v):
        self.v = v
        Clothes.sum_cloth += self.calc_cloth

    @property
    def calc_cloth(self):
        return self.v / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, h):
        self.h = h
        Clothes.sum_cloth += self.calc_cloth

    @property
    def calc_cloth(self):
        return 2 * self.h + 0.3


coat_1 = Coat(52)
coat_2 = Coat(65)
costume_1 = Costume(30)
print(Clothes.sum_cloth)
print(Coat.sum_cloth)
print(Costume.sum_cloth)
# Вывод последних трех строчек получился одинаковым. Получается при наследовании атрибут класса остается общим
# и для дочерних классов?
