# Еще один возможный вариант программы:
# Запрос стартого и прогнозируемого пробега
current_dist = float(input('Введите пробег в первый день, км: '))
final_dist = float(input('Введите ожидаемый пробег, км: '))
runday = 0 # номер дня бега
# Цикл изменяет номер дня и пробегаемую дистанцию
while True:
    runday += 1
    if current_dist < final_dist:
        current_dist *= 1.1
    else:
        break
print(f'{runday} - номер дня, в который результат составит не менее {final_dist} км')