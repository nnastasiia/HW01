# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

f_5 = open(r"C:\Users\Asus\Desktop\домашка\file_num.txt", 'w+')
f_5.write(input("enter any numbers: "))
f_5.seek(0, 0)
content = f_5.read()


def func_1():
    n = str(content).split()
    res = 0
    for i in range(len(n)):
            res += int(n[i])
    print(f'your sum is: {res}')


func_1()
