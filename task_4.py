from time import perf_counter

start_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
uniqe_num = set()
repeated_num = set()
# через множества
start = perf_counter()
for el in start_list:
    if el in repeated_num:
        continue
    elif el in uniqe_num:
        uniqe_num.discard(el)
        repeated_num.add(el)
    else:
        uniqe_num.add(el)
result_list = [num for num in start_list if num in uniqe_num]
print(result_list)
print('1111', (perf_counter() - start)*100000)

# через словари и метод my_dict2.keys()
start = perf_counter()
my_dict = {}
for el in start_list:
    if  el in my_dict.keys():
        my_dict[el] = -1
    else:
        my_dict[el] = 1
result_list = [num for num in my_dict.keys() if my_dict[num] == 1]
print(result_list)
print('2222', (perf_counter() - start)*100000)

# через словари и метод my_dict.get(el)
start = perf_counter()
my_dict = {}
for el in start_list:
    if  my_dict.get(el) == None:
        my_dict[el] = 1
    else:
        my_dict[el] = 0
result_list = [num for num in my_dict.keys() if my_dict[num] == 1]
print(result_list)
print('3333', (perf_counter() - start)*100000)
