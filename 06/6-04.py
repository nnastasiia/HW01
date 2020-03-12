class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} started'

    def stop(self):
        return f'{self.name} stopped'

    def turn_right(self):
        return f'{self.name} is turning right'

    def turn_left(self):
        return f'{self.name} is turning left'

    def show_speed(self):
        return f'your speed is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):

        if self.speed > 40:
            return f' driving at {self.name} is too cool for you'
        else:
            return f'calm down'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        return f'your speed is {self.speed}'

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'driving at {self.name} is too cool for you'
        else:
            return f'your speed is {self.speed}'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
    def show_speed(self):
        return f'your speed is {self.speed}'

    def police(self):
        if self.is_police:
            return f'{self.name} is dangerous'
        else:
            return f'{self.name} is cute'


mers = SportCar(100, 'black', 'mers', False)
hen = TownCar(40, 'red', 'hen', False)
audi = WorkCar(50, 'white', 'audi', False)
ford = PoliceCar(110, 'grey', 'ford', True)

print(f'{hen.name} is {hen.color}')
print(audi.show_speed())
print(hen.show_speed())
print(ford.police())
