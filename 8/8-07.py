class ComplexNumbers:
    def __init__(self, x, y, *args):
        self.x = x
        self.y = y
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'sum equals ')
        return f'z = {self.x + other.x} + {self.y + other.y} * i'

    def __mul__(self, other):
        print(f'product of two numbers equals ')
        return f'z = {self.x * other.x - (self.y * other.y)} + {self.y * other.x} * i'

    def __str__(self):
        return f'z = {self.x} + {self.y} * i'


z_1 = ComplexNumbers(9, 4)
z_2 = ComplexNumbers(8, 2)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)