import numpy as np


class BlockSimulationModel:
    def __init__(self,
                 angle: float = 45,
                 width: float = 0.3,
                 coefficient_still: float = None,
                 coefficient_moving: float = None,
                 block1_position: (float, float) = None,
                 block2_position: (float, float) = None):
        self.__angle = angle
        self.__width = width
        self.__coefficient_still = coefficient_still
        self.__coefficient_moving = coefficient_moving
        self.__block1_position = block1_position
        self.__block2_position = block2_position

    ### Getter ###
    @property
    def angle(self):
        return self.__angle

    @property
    def width(self):
        return self.__width

    @property
    def coefficient_still(self):
        return self.__coefficient_still

    @property
    def coefficient_moving(self):
        return self.__coefficient_moving

    # TODO: Refac
    def get_opposite_length(self, adjacent):
        return np.tan(np.radians(self.__angle)) * adjacent

    ### Setter ###
    @angle.setter
    def angle(self, value):
        self.__angle = value

    @width.setter
    def width(self, value):
        self.__width = value

    @coefficient_still.setter
    def coefficient_still(self, value):
        self.__coefficient_still = value

    @coefficient_moving.setter
    def coefficient_moving(self, value):
        self.__coefficient_still = value
