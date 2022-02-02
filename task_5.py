with open("task_5.txt", "w", encoding="utf-8") as f:
    f.write('5 5 26 37 98 25 67')
with open("task_5.txt", "r", encoding="utf-8") as f:
    number_list = f.readline().split()
    for i in range(len(number_list)):
        number_list[i] = float(number_list[i])
print(f'Сумма чисел в файле: {sum(number_list)}')
