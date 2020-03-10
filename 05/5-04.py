# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

f_3 = open(r"C:\Users\Asus\Desktop\домашка\file_3.txt", 'r')
f_4 = open(r"C:\Users\Asus\Desktop\домашка\file_3_new.txt", 'w')
my_dict = {1: 'один', 2: 'два', 3: 'три', 4: 'четыре'}
n = 1
for line in f_3:
    a = str(line).split(" ")
    a.pop(0)
    a.insert(0, my_dict[n])
    n += 1
    f_4.writelines(' '.join(a))
f_4.close()
f_3.close()
