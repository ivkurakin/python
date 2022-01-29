from sys import argv

hours = int (argv[1])
pay_per_hour = int (argv[2])
bonus = int (argv[3])
wage = hours * pay_per_hour + bonus
print(f'Заработная плата: {wage}')
