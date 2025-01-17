import numpy as np


class TriangleModel:
    def __init__(self, angle: float = None):
        self.__angle = angle

    def __repr__(self):
        return f'Angle in Deg: {self.__angle} and in Rad: {np.radians(self.__angle)}.'

    @property
    def angle(self):
        return self.__angle

    @ngle.setter
    def angle(self, value):
        self.__angle = value

    def get_opposite_length(self, adjacent):
        return np.tan(np.radians(self.__angle)) * adjacent
