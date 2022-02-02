import json

sum_profit = 0  # Суммарная прибыль компаний, работающих в плюс
num_profit = 0  # Количество компаний, работающих в плюс
company_dict = {}  # словарь для компаний
average_dict = {}  # словарь для среднего значения
final_list = []
with open("text_7.txt", "r", encoding="utf-8") as f:
    for line in f:
        profit = float(line.split()[2]) -  float(line.split()[3])
        company_dict[line.split()[0]] = profit
        print(f"Прибыль {line.split()[1]} {line.split()[0]}: {profit}")
        if profit > 0:
            sum_profit += profit
            num_profit += 1
    print(f"Средняя прибыль: {sum_profit / num_profit}")
    average_dict['average_profit'] =  sum_profit / num_profit
    final_list = [company_dict, average_dict]
    print(final_list)
with open("task_7.json", "w", encoding="utf-8") as f:
    json.dump(final_list, f)
