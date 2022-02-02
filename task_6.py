hours_list = []  # список суммарного времени, соотносится со списком предметов
subject_list = []  # список предметов
with open("text_6.txt", "r", encoding="utf-8") as f:
    for line in f:
        sum = 0
        cur_list = []
        new_list = []
        cur_list = line.split()  # разбиваем строку по пробелу
        for i in range(1, len(cur_list)):
            new_list = cur_list[i].split('(')  # разбиваем строку по скобке
            if new_list[0].isdigit():  # после разбиения число будет находится во вложенном списке под инд. 0
                new_list[0] = int(new_list[0])
                sum += new_list[0]
        if sum != 0:
            hours_list.append(sum)
            subject_list.append(cur_list[0])
    final_dict = {subject_list[i]:hours_list[i] for i in range(len(subject_list))}
    print(final_dict)
