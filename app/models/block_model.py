
class BlockModel:
    def __init__(self, width: float = None):
        self.__width = width

    def __repr__(self):
        return f'Width: {self.__width}'

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
