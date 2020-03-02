def f_1():
    sum_res = 0
    e = False
    while e is False:
        n = input('Enter numbers or S to quit - ').split()

        res = 0
        for i in range(len(n)):
            if n[i] == 'S':
                e = True
                break
            else:
                res += int(n[i])
        sum_res += res
        print(f'Current sum is {sum_res}')
    print(f'Final sum is {sum_res}')


f_1()
