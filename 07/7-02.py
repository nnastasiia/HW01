# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3).
# Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.


class Sewing:
    def __init__(self, v, h):
        self.h = h
        self.v = v

    def coat(self):
        return self.v / 6.5 + 0.5

    def costume(self):
        return self.h * 2 + 0.3

    @property
    def all(self):
        return str(f'amount of fabric: {(self.v / 6.5 + 0.5) + (self.h * 2 + 0.3)}')


class Coat(Sewing):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.sq_coat = self.v / 6.5 + 0.5

    def __str__(self):
        return f'amount of fabric for coat: {self.sq_coat}'


class Costume(Sewing):
    def __init__(self, v, h):
        super().__init__(v, h)
        self.sq_costume = self.h * 2 + 0.3

    def __str__(self):
        return f'amount of fabric for costume: {self.sq_costume}'


c = Coat(2, 1)
cm = Costume(2, 1)
print(c)
print(cm)
print(c.all)
