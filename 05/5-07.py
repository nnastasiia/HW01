# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки,в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь(со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта: [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]


import json

profit = {}
pr = {}
pro = 0
average_profit = 0
i = 0
with open(r"C:\Users\Asus\Desktop\домашка\file_7.txt", 'r') as file:
    for line in file:
        firm, form, earn, cost = line.split()
        profit[firm] = int(earn) - int(cost)
        if profit.setdefault(firm) >= 0:
            pro += profit.setdefault(firm)
            i += 1
    if i != 0:
        average_profit = pro / i
        print(f'average profit - {average_profit:.2f}')
    else:
        print(f'everyone failed')
    pr = {'average profit': round(average_profit)}
    profit.update(pr)
    print(f'profitability - {profit}')

with open('file_7.json', 'w') as write_js:
    json.dump(profit, write_js)

    js_str = json.dumps(profit)
    print(f'file created: ', f' {js_str}')
