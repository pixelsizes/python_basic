class Cell:
    __number = 0

    def __init__(self, number):
        self.__number = number

    def __add__(self, other):
        return Cell(self.__number + other.__number)

    def __sub__(self, other):
        if self.__number < other.__number:
            raise ArithmeticError('Cant subtract')

        return Cell(self.__number - other.__number)

    def __mul__(self, other):
        return Cell(self.__number * other.__number)

    def __truediv__(self, other):
        return Cell(self.__number // other.__number)

    def make_order(self, rows):
        first_part = max(0, (self.__number - 1) // rows)
        return ('*' * rows + '\n') * first_part + ('*' * (self.__number - first_part * rows))

    def __str__(self):
        return f'{self.__number}'

str = Cell(0).make_order(5)
str = Cell(11).make_order(5)
str = Cell(10).make_order(5)
str = Cell(0).make_order(5)
str = Cell(1).make_order(5)
str = Cell(2).make_order(5)
str = Cell(4).make_order(5)
str = Cell(5).make_order(5)
str = Cell(6).make_order(5)
print(Cell(15).make_order(5))
print(Cell(15) - Cell(16))
