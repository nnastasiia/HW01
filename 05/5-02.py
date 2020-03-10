#  Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

f_1 = open(r"C:\Users\Asus\Desktop\домашка\file_1.txt", 'r')
my_list = f_1.readlines()
print(my_list)
print("number of strings: ", len(my_list))
for el in my_list:
    n = 0
    a = str(el).split(" ")
    n += 1
    print("number of words in string ", n, "is", len(a))
    








