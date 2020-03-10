f_1 = open("my_file.txt", 'w')
print("do not enter anything to quit")
while True:
    my_list = []
    a = input("enter new string: ")
    if a != "":
        my_list.append(a + '\n')
        f_1.writelines(my_list)
    else:
        print("you quited")
        break
f_1.close()
