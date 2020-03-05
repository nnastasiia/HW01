# Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.

from itertools import count, cycle
for el in count(6):
    if el > 10:
        break
    print(el)

my_list = [1, 'aa', 2, 'bb', 3, 'cc']
n = 0
for i in cycle(my_list):
    if n > 12:
        break
    print(i)
    n += 1

