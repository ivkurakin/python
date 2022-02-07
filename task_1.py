import time
from colorama import Fore, Style


class TrafficLight:
    __color = 'red'


    def running(self):
        for i in range(3):
            print(Fore.RED + TrafficLight.__color)
            time.sleep(7)
            TrafficLight.__color = 'yellow'
            print(Fore.YELLOW + TrafficLight.__color)
            time.sleep(2)
            TrafficLight.__color = 'green'
            print(Fore.GREEN + TrafficLight.__color)
            time.sleep(30)
            TrafficLight.__color = 'red'


light = TrafficLight()
light.running()
