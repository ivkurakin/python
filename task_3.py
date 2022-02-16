class MyOwnErr(Exception):
    def __init__(self, txt):
        pass


def check_float(ch_str):
    if ch_str.count('.') == 1 and ch_str.split('.')[0].isdigit() and ch_str.split('.')[1].isdigit():
        return True
    else:
        return False


final_list = []
user_numbers = ''
while True:
    try:
        user_numbers = input('Введите целое число или "stop: ')
        num_list = None
        if len(user_numbers) == 0:
            raise MyOwnErr('Вы ничего не ввели!')
        if user_numbers != 'stop':
            num_list = user_numbers.split(' ')
            if len(num_list) > 1:
                raise MyOwnErr('Вы ввели много чисел!')
            if not user_numbers.isdigit() and check_float(user_numbers) == False and user_numbers != 'stop':
                raise MyOwnErr('Вы ввели не целое число!')
        else:
            break
    except MyOwnErr as err:
        print(err)
    else:
        final_list.append(float(user_numbers))
print(f"Список: {final_list}")
