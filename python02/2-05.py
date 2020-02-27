new_list = [100, 78, 45, 30, 17, 5]
n = int(input("Enter new value: "))
a = new_list.count(n)
for el in new_list:
    if a > 0:
        new_list.insert(new_list.index(n) + a, n)
        break
    else:
        if n > el:
            new_list.insert(new_list.index(el), n)
            break
        elif n < new_list[(len(new_list) - 1)]:
            new_list.append(n)
print(new_list)





