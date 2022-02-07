class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_mass(self, mass_per, depth):
        full_mass = self._length * self._width * mass_per * depth
        return full_mass


user_road = Road(20, 5000)
print(user_road.get_mass(25, 5))
