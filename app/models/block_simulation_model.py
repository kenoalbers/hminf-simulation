
class BlockSimulationModel:
    def __init__(self,
                 angle: float = None,
                 width: float = None,
                 coefficient_still: float = None,
                 coefficient_moving: float = None):
        self.__angle = angle
        self.__width = width
        self.__coefficient_still = coefficient_still
        self.__coefficient_moving = coefficient_moving

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
