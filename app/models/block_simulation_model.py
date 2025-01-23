import numpy as np


class BlockSimulationModel:
    def __init__(self,
                 angle: float = 45,
                 width: float = 0.3,
                 coefficient_still: float = 0.3,
                 coefficient_moving: float = 0.3,
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

    @property
    def block1_position(self):
        return self.__block1_position

    @property
    def block2_position(self):
        return self.__block2_position

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

    @block1_position.setter
    def block1_position(self, value):
        self.__block1_position = value

    @block2_position.setter
    def block2_position(self, value):
        self.__block2_position = value

    # Helper Methods
    def get_opposite_length(self, adjacent):
        return np.tan(np.radians(self.__angle)) * adjacent

    def get_block1_center(self):
        center_x = self.block1_position[0] / self.width
        center_y = self.block1_position[1] / 0.1
        return center_x, center_y
