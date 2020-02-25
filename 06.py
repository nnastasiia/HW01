# zadacha6

a = float(input("start: "))
b = float(input("finish: "))
day = 1
if a > b:
    print(day)
while a < b:
    a = a + a/10
    day += 1
print(day)
