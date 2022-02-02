'''Сделал два варианта.
Первый добавляет записи в конце файла (task1_1.txt).
Второй при каждом выполнении перезаписывает файл (task1_2.txt).'''

user_str = None
my_list = []
while user_str != '':
    user_str = input('Введите строку: ')
    if user_str != '':
        with open ("task1_1.txt", "a", encoding="utf-8") as f:
            print(user_str, end='\n', file=f)
        my_list.append(user_str + '\n')
        with open ("task1_2.txt", "w", encoding="utf-8") as f2:
            f2.writelines(my_list)
