def divide (num_1, num_2):
    """Возвращает частное от деления.

    Позиционные параметры:
    num_1 -- делимое
    num_2 -- делитель
    """
    try:
        return num_1 / num_2
    except ZeroDivisionError:
        print('На ноль делить нельзя!')


user_dividend= float(input('Введите делимое (в десятичных дробях используется "."): '))
user_divider= float(input('Введите делитель (в десятичных дробях используется "."): '))
if divide (user_dividend, user_divider):  # чтоб при делении на 0 не печаталосm None
    print(f'Результат: {divide (user_dividend, user_divider)}')
