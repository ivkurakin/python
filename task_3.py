my_dict = {'зима' : [1, 2, 12], 'весна' : [3, 4, 5],
           'лето' : [6, 7, 8],'осень' : [9, 10, 11]}

while True:
    month = input('Введите целое число от 1 до 12: ')
    if month.isdigit() and int(month) >= 1 and int(month) <= 12:
        month = int(month)
        for key in my_dict.keys(): # проход по ключам
            if month in my_dict[key]: # поиск в списке
                print(f'Время года: {key}')
                break
        break
    else:
        print('Некорректный ввод!')
        continue