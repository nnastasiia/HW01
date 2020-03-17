# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.


class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    @property
    def __add__(self):
        matrix = [[1, 1, 1],
                  [1, 1, 1],
                  [1, 1, 1]]

        for i in range(len(self.list_1)):

            for el in range(len(self.list_2[i])):
                matrix[i][el] = self.list_1[i][el] + self.list_2[i][el]
        return str('\n'.join(['\t'.join([str(el) for el in i]) for i in matrix]))

    def __str__(self):
        return str('\n'.join(['\t'.join([str(el) for el in i]) for i in matrix]))


my_matrix = Matrix([[4, 2, 5],
                    [5, 3, 1],
                    [7, 9, 2]],
                   [[6, 8, 5],
                    [5, 7, 9, ],
                    [3, 1, 8]])

print(my_matrix.__add__)
