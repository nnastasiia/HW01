class Null:
    def __init__(self, m, n):
        self.m = m
        self.n = n

    @staticmethod
    def divide_by_zero(m, n):
        try:
            return m / n
        except:
            return (f"do not divide by zero")


div = Null(15, 5)
print(Null.divide_by_zero(1, 0))
print(div.divide_by_zero(56, 2))
