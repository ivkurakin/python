from itertools import count, cycle

for el in count(2, 3):
    if el > 99:
        break
    print(el)

my_list = [3, 1, 4, 1, 5, 9]
iter_num = 0
for el in cycle(my_list):
    if iter_num > 19:
        break
    print(el)
    iter_num += 1

