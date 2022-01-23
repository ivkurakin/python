my_list = []
while True:
    num = input('Введите натуральное число или введите "-1" для выхода: ')
    if num != '-1':
        if num.isdigit() and num != '0':
            num = int(num)
            if len(my_list):  # проверяем, что это не первый ввод
                if num <= my_list[len(my_list)-1]: # проверяем целесообразность прохода по элементам списка
                    my_list.append(num)  # добавляем в конец списка, если нет
                    print(my_list)
                else:
                    for el in my_list: # проход по циклу
                        if num > el: # вставляем на место числа,если оно строго меньше
                            my_list.insert(my_list.index(el), num)
                            print(my_list)
                            break
            else:
               my_list.append(num)  # ввод первого числа
               print(my_list)
        else:
            print('Некорректный ввод!')
            print(my_list)
            continue
    else:
        break
