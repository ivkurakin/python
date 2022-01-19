number = int(input('Введите целое положительное число: '))  # Запрос числа
max_num = 0
# Цикл перебирает цифры, образующие число.
while (number > 0):
    cur_num = number % 10  # текущая цифра
    if cur_num >  max_num:  # сравнение с максимальным на  данную итерацию
        max_num =  cur_num # перезапись максимального
    number = number // 10
print(max_num)



