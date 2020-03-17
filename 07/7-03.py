class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __add__(self, other):
        return f'add: {self.quantity + other.quantity}'

    def __sub__(self, other):
        sub = self.quantity - other.quantity
        if sub > 0:
            return f'smaller cell equals {sub} cells'
        else:
            return f'cell died'

    def __truediv__(self, other):
        return self.quantity // other.quantity

    def __mul__(self, other):
        return self.quantity * other.quantity

    def make_order(self, row):
        result = ''
        for i in range(int(self.quantity / row)):
            result += '*' * row + '\n'
        result += '*' * (self.quantity % row) + '\n'
        return result


cell = Cell(49)
cell_2 = Cell(10)
print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)
print(cell.make_order(10))