n = int(input("enter month number: "))
month_dict = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'June',
              7: 'July', 8: 'Aug', 9: 'Sept', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
month_list = list(month_dict.keys())
n == month_list.index(n + 1)
while 3 <= n <= 8:
    if 3 <= n <= 5:
        print(f'{month_dict.get(n)} is spring month')
        break
    elif 6 <= n <= 8:
        print(f'{month_dict.get(n)} is summer month')
        break
else:
    if 9 <= n <= 11:
        print(f'{month_dict.get(n)} is autumn month')
    else:
        print(f'{month_dict.get(n)} is winter month')


