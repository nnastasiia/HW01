class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки {self.title}'


class Pen(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{self.title} не пишет, не бери'


class Pencil(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{self.title} есть только красный'


class Handle(Stationary):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'{self.title}? ну кто им рисует?'


pen = Pen('ручка')
handle = Handle('маркер')
pencil = Pencil('карандаш')
print(pen.draw())
print(pencil.draw())
print(handle.draw())
