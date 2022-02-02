name_list = []
salary_list = []
with open("text_3.txt", "r", encoding="utf-8") as f:
    for line in f:
        new_list = []
        new_list = line.split()
        new_list[1] = float (new_list[1])
        salary_list.append(new_list[1])
        if  new_list[1] < 20000:
            name_list.append(new_list[0])
print(f'Список сотрудников с зарплатой менее 20тыс.: ')
for el in name_list:
    print(el)
print(f'Средняя зарплата: {sum(salary_list) / len(salary_list):.2f}')
