def get_upper(user_word):
    """Возвращает слово с заглавной буквы.
    Реализовано с помощью встроенной функции.

    Позиционные параметры:
    user_word -- слово
    """
    return user_word.capitalize()


def get_upper_exp (user_word):
    """Возвращает слово с заглавной буквы.
    Реализовано без помощи встроенной функции.

    Позиционные параметры:
    user_word -- слово
    """
    new_string = ''
    for i in range(len(user_word)):
        if i == 0:
            new_string += chr(ord(user_word[0]) - 32)
        else:
            new_string += user_word[i]
    return new_string


words_list = []  # список для функции get_upper
words_list_exp = [] # список для функции get_upper_exp
user_str = ''
enter = False
while enter != True:
    user_str = input('Введите слова латинскими буквами через пробел: ')
    for el in user_str:
        if (97 > ord(el) or  ord(el) > 122) and ord(el) != 32: # проверка корректности введеной строки
            print(f'Некорректный ввод!')
            enter = False
            break
        else:
            enter = True
words_list = user_str.split(' ')
words_list_exp = user_str.split(' ')
for i in range(len(words_list)):
    words_list[i] = get_upper(words_list[i])
    words_list_exp[i] = get_upper_exp(words_list_exp[i])
print(' '.join(words_list))
print(' '.join(words_list_exp))
