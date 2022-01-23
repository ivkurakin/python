my_list = []
my_dict = {}
name_list = []
price_list = []
number_list = []
per_list = []
num_item = 0
while True:
    name = input('Введите название товара: ')
    if name != '-1':
        while True:
            price = input('Введите цену: ')
            if price.isdigit():
                price = int (price)
                break
            else:
                print('Некорректный ввод!')
                continue
        while True:
            number = input('Введите количество: ')
            if number.isdigit():
                number = int (number)
                break
            else:
                print('Некорректный ввод!')
                continue
        per = input('Введите ед. изм.: ')
        my_dict = {'Название' : name, 'Цена' : price, 'Количество' : number,'Ед.' : per}
        num_item += 1
        my_tuple = (num_item, my_dict) # почему прошла эта операция при второй итерации?
        # на каждой итерации я создаю новый локальный кортеж, а не изменяю старый?
        my_list.append(my_tuple)
    else:
        break
print('Структура: ', my_list)
for el in my_list:
    name_list.append(el[1].get('Название'))
    price_list.append(el[1].get('Цена'))
    number_list.append(el[1].get('Количество'))
    per_list.append(el[1].get('Ед.'))
final_dict = {'Название' : name_list, 'Цена' : price_list,
              'Количество' : number_list,'Ед.' : per_list}
print('Словарь: ', final_dict)
