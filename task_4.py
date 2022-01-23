user_str = input('Введите слова через пробел: ')
my_list = user_str.split()
for ind, el in enumerate(my_list):
    print(ind + 1, el[:10])
