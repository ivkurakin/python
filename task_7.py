def fact(n):
    cur_list = []
    # Создаем список cur_list из факториалов
    for i in range(1, n+1):
        result = 1
        for k in range(1, i+1):
            result *= k
        cur_list.append(result)
    for el in cur_list:
        yield el


for el in fact(5):
    print(el)

for el in fact(10):
    print(el)

