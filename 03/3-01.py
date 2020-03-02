def f_1(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "do not divide by zero"


a = (int(input("enter first number ")))
b = (int(input("enter first number ")))

print(f_1(a, b))
