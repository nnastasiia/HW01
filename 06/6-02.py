# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина*ширина*масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
# Проверить работу метода.
# Например: 20м*5000м*25кг*5см = 12500 т

class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def sq(self):
        return self._length * self._width


class Mass(Road):
    def __init__(self, _length, _width, thickness, mass):
        super().__init__(_length, _width)
        self.thickness = thickness
        self.mass = mass

    def result(self):
        return Road.sq(self) * self.thickness * self.mass


m = Mass(1000, 10, 5, 25)
print(m.result())
