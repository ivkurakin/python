# Запрос выручки и издержек
revenue = float(input('Введите выручку: '))
costs = float(input('Введите издержки: '))
# Оценка работы фирмы
if (revenue - costs) > 0:
    print('Фирма работает с прибылью')
    print(f"Рентабельность составляет: {((revenue - costs) /  revenue):.2f}")  # расчет рентабельности
    num_employees  = int(input('Ввведите количество сотрудников в фирме: ')) # запрос количества сотрудников
    profit_per_employee  =  (revenue - costs) / num_employees  # расчет прибыли на одного сотрудника
    print(f"Прибыль на одного сотрудника: {profit_per_employee:.2f}")
elif (revenue - costs) < 0:
    print('Фирма работает с убытком')
else:
     print('Фирма работает в 0')