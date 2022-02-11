class Cell:
    def __init__(self, num_cell):
        self.num_cell = num_cell

    def __add__(self, other):
        return Cell(self.num_cell + other.num_cell).make_order(8)

    def __sub__(self, other):
        if self.num_cell - other.num_cell > 0:
            return Cell(self.num_cell - other.num_cell).make_order(9)
        else:
            print('Вычитание невозможно!')
            return 21 * '-'

    def __mul__(self, other):
        return Cell(self.num_cell * other.num_cell).make_order(21)

    def __truediv__(self, other):
        return Cell(self.num_cell / other.num_cell)

    def __floordiv__(self, other):
        return Cell(self.num_cell // other.num_cell).make_order(3)

    def make_order(self, num_row):
        count_num = self.num_cell
        while count_num // num_row:
            print(num_row * '*')  # можно было через for in
            count_num -= num_row
        for i in range(self.num_cell % num_row):
            print('*', end='')
            print()
        return 21*'-'


cell_1 = Cell(35)
cell_2 = Cell(6)
print('Add:')
print(cell_1 + cell_2)
print('Sub 1-2:')
print(cell_1 - cell_2)
print('Sub 2-1:')
print(cell_2 - cell_1)
print('Mul:')
print(cell_1 * cell_2)
print(f'TrueDiv: {(cell_1 / cell_2).num_cell}')
print('FloorDiv:')
print(cell_1 // cell_2)
