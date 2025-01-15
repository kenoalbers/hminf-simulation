

class TriangleModel:
    def __init__(self, angle):
        self.angle = angle

    @property
    def angle(self):
        return self.__angle

    @angle.setter
    def angle(self, value):
        self.__angle = value
        # Raise ValueError if angle not correct


