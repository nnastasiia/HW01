my_str = str(input("enter sentence: "))
words = list(my_str.split(' '))
for ind, el in enumerate(words, 1):
    print(f'{ind}.{el[0:10]}')






