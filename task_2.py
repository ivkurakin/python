my_list = []
el_ls = 0
while el_ls != '-1': # выход из цикла по вводу -1 пользователем
    el_ls = input('Введите элемент списка или введите -1 для вывода результата: ')
    if el_ls != '-1':
        my_list.append(el_ls)
    else:
        for i in range(1, len(my_list), 2): # проход по нечетным индексам
            my_list[i], my_list[i - 1] = my_list[i - 1], my_list[i]
print(my_list)
