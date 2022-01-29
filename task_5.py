from functools import reduce


def my_func(num1, num2):
    ''' Функция возвращает произведение двух чисел.

    Позиционные параметры:
    num_1 -- 1-е число,
    num_2 -- 2-е число'''
    return num1 * num2


new_list = [el for el in range(100, 1001, 2)]  # Создаем список из четных чисел
print(reduce(my_func, new_list))
