class MyOwnErr(Exception):
    def __init__(self, txt):
        pass


try:
    user_numbers = input('Введите делимое и делитель через пробел: ')
    num_list = user_numbers.split(' ')
    if len(num_list) > 2:
        raise MyOwnErr('Вы ввели много чисел!')
    if len(num_list) < 2:
        raise MyOwnErr('Вы ввели мало чисел!')
    num1 = float(num_list[0])
    num2 = float(num_list[1])
    if num2 == 0:
        raise MyOwnErr('Деление на "0" невозможно!')
except ValueError:
    print('Вы ввели не числа!')
except MyOwnErr as err:
    print(err)
else:
    print(f"Результат: {num1 / num2}")
