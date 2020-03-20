class Storage:

    def __init__(self, name, price, number, number_of_lists, *args):
        self.name = name
        self.price = price
        self.number = number
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'model': self.name, 'price': self.price, 'amount': self.number}

    def __str__(self):
        return f'{self.name} price {self.price} amount {self.number}'

    def reception(self):
        try:
            unit = input(f'enter name ')
            unit_p = int(input(f'enter price '))
            unit_q = int(input(f'enter amount '))
            unique = {'model': unit, 'price': unit_p, 'amount': unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'list  {self.my_store}')
        except:
            return f'error'

        print(f'press Q to exit')
        q = input()
        if q == 'Q':
            self.my_store_full.append(self.my_store)
            print(f'everything  {self.my_store_full}')
            return f'closed'
        else:
            return Storage.reception(self)


class Printer(Storage):
    def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(Storage):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(Storage):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'


unit_1 = Printer('hp', 1000, 4, 12)
unit_2 = Scanner('hp', 1200, 11, 10)
unit_3 = Copier('hp', 1500, 2, 15)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())
