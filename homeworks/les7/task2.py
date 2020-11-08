"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс)
этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся
пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""


class Clothes:
    __consumption = 0.0

    def __init__(self, name):
        self.__name = name

    @property
    def consumption(self):
        raise NotImplemented


class Coat(Clothes):
    __V = 0.0

    def __init__(self, V):
        self.__V = V
        super().__init__('Coat')

    @property
    def consumption(self):
        return self.__V / 6.5 + 0.5


class Dress(Clothes):
    __H = 0.0

    def __init__(self, H):
        self.__H = H
        super().__init__('Dress')

    @property
    def consumption(self):
        return 2 * self.__H + 0.3


coat = Coat(2)
dress = Dress(3)

print(coat.consumption)
print(dress.consumption)
