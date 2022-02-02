num_str = 0
with open("task1_1.txt", "r", encoding="utf-8") as f:
    for line in f:
        num_str += 1
        print (f'В строке {num_str}: {len(line.split())} сл.')
print (f'Всего строк: {num_str}')
