def get_sum(cur_total, cur_list):
    """Возвращает сумму чисел (из списка) с учетом текущей.

    Позиционные параметры:
    cur_total -- текущая сумма
    cur_list  -- список чисел для суммирования
    """
    cur_total += sum(cur_list)
    return cur_total


def make_list_float(cur_list):
    """Преобразует строки из переданного списка в формат float

    Позиционные параметр:
    cur_list -- список строк для преобразования
    """
    for i in range (len(cur_list)):
        cur_list[i] = float(cur_list[i])
    return cur_list


user_numbers = []
mod_numbers = []
cur_sum = 0
while 'Q' not in user_numbers:
    user_numbers = input('Введи числа через пробел или Q для выхода: ').split(' ')
    if 'Q' in user_numbers:
        mod_numbers = user_numbers[:user_numbers.index('Q')] # добавляем в новый список, введенные значения до 'Q'
        mod_numbers = make_list_float(mod_numbers)
        cur_sum = get_sum(cur_sum, mod_numbers)
        print(f'Сумма равна {cur_sum}')
    else:
        user_numbers = make_list_float(user_numbers)
        cur_sum = get_sum(cur_sum, user_numbers)
