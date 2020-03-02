def my_func(val):
    val = [a, b, c]
    val.remove(min(a, b, c))
    return sum(val)
a = (int(input("enter first number ")))
b = (int(input("enter second number ")))
c = (int(input("enter third number ")))
print(my_func(val=[a, b, c]))
