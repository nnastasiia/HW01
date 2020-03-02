# первый вариант:
def my_func(x, y):
    return x ** y


x = float(input("enter any number "))
y = int(input("enter any negative number "))
print(my_func(x, y))

# корректно ли оставлять у отрицательным для расчёта, или стоит записать как 1 / х**abs(y) ?