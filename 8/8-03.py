class Number:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                i = int(input('enter values '))
                self.my_list.append(i)
                print(f'your list {self.my_list} ')
            except:
                print(f"not only numbers")
                again = input(f'to try again press A ')
                if again == 'A':
                    print(try_except.my_input())
                else:
                    return f'closed'

try_except = Number(9)
print(try_except.my_input())
