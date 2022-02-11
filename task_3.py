class Cell:
    def __init__(self, num_cell):
        self.num_cell = num_cell

    def __add__(self, other):
        return Cell(self.num_cell + other.num_cell)

    def __sub__(self, other):
        if self.num_cell - other.num_cell > 0:
            return Cell(self.num_cell - other.num_cell)
        else:
            print('Вычитание невозможно!')

    def __mul__(self, other):
        return Cell(self.num_cell * other.num_cell)

    def __truediv__(self, other):
        return Cell(self.num_cell / other.num_cell)

    def __floordiv__(self, other):
        return Cell(self.num_cell // other.num_cell)

    def make_order(self, num_row):
        count_num = self.num_cell
        while count_num // num_row:
            print(num_row * '*')  # можно было через for in
            count_num -= num_row
        for i in range(self.num_cell % num_row):
            print('*', end='')
        print()


cell_1 = Cell(35)
cell_2 = Cell(6)
print('Add:')
(cell_1 + cell_2).make_order(8)
print('Sub 1-2:')
if type(cell_1 - cell_2) == Cell:
    (cell_1 - cell_2).make_order(9)
print('Sub 2-1:')
if type(cell_2 - cell_1) == Cell:
    (cell_2 - cell_1).make_order(9)
print('Mul:')
(cell_1 * cell_2).make_order(21)
print(f'TrueDiv: {(cell_1 / cell_2).num_cell}')
print('FloorDiv:')
(cell_1 // cell_2).make_order(3)
