#  Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
#  Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
#  Выполнить подсчет средней величины дохода сотрудников.

with open(r"C:\Users\Asus\Desktop\домашка\file_2.txt", 'r') as my_file:
    sal = []
    a = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            a.append(i[0])
        sal.append(i[1])
print(f'salary lower than 20000 {a}, average {sum(map(int, sal)) / len(sal)}')
