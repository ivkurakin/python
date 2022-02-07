class Car:

    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала!')

    def stop(self):
        print('Машина остановилась!')

    def turn(self, direction):
        print(f'Машина повернула на{direction}')

    def show_speed(self):
        print(f'Текущая скорость: {self.speed}')


class TownCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 60:
            print(f'Текущая скорость: {self.speed}. Превышение!')
        else:
            print(f'Текущая скорость: {self.speed}')


class SportCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class WorkCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 40:
            print(f'Текущая скорость: {self.speed}. Превышение!')
        else:
            print(f'Текущая скорость: {self.speed}')


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


print('Town car без превышения:')
town_car1 = TownCar(50, 'red', 'bmw')
print(town_car1.name)
print(town_car1.color)
print(town_car1.speed)
print(town_car1.is_police)
town_car1.go()
town_car1.stop()
town_car1.turn('лево.')
town_car1.show_speed()

print('Town car с превышением:')
town_car2 = TownCar(70, 'yellow', 'opel')
print(town_car2.name)
print(town_car2.color)
print(town_car2.speed)
print(town_car2.is_police)
town_car2.go()
town_car2.stop()
town_car2.turn('лево.')
town_car2.show_speed()

print('Sport car:')
sport_car = SportCar(140, 'red', 'ferrari')
print(sport_car.name)
print(sport_car.color)
print(sport_car.speed)
print(sport_car.is_police)
sport_car.go()
sport_car.stop()
sport_car.turn('лево.')
sport_car.show_speed()

print('Work car без превышения:')
work_car1 = WorkCar(30, 'black', 'lada')
print(work_car1.name)
print(work_car1.color)
print(work_car1.speed)
print(work_car1.is_police)
work_car1.go()
work_car1.stop()
work_car1.turn('право.')
work_car1.show_speed()

print('Work car с превышением:')
work_car2 = WorkCar(41, 'blue', 'skoda')
print(work_car2.name)
print(work_car2.color)
print(work_car2.speed)
print(work_car2.is_police)
work_car2.go()
work_car2.stop()
work_car2.turn('право.')
work_car2.show_speed()

print('Police car:')
police_car = PoliceCar(85, 'white', 'saab')
print(police_car.name)
print(police_car.color)
print(police_car.speed)
print(police_car.is_police)
police_car.go()
police_car.stop()
police_car.turn('лево.')
police_car.show_speed()
