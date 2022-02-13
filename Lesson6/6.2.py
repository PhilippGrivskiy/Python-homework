class Road:
    def __init__(self, width, length):
        self._width = width
        self._length = length

    @property
    def square(self):
        return self._length * self._width

    def get_weight_of_asphalt(self, weight_ratio, thikness):
        asphalt = self.square * weight_ratio * thikness
        return asphalt


my_road = Road(20, 5000)
print(my_road.get_weight_of_asphalt(25, 0.5))