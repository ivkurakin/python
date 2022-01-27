def my_func(num_1, num_2, num_3):
    """Возвращает сумму двух наибольших чисел.

    Позиционные параметры:
    num_1 -- первое число
    num_2 -- второе число
    num_3 -- третье число
    """
    my_list = [num_1, num_2, num_3]
    return sum(my_list) - min(my_list)


print(f'Сумма: {my_func(345, 23, 100)}')
print(f'Сумма: {my_func(47.5, 10, 5.3)}')
