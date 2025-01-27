
class ForceModel:
    def __init__(self,
                 g_force: float = 0.0,
                 grade_force: float = 0.0,
                 friction_force_still: float = 0.0,
                 friction_force_moving: float = 0.0,
                 acceleration: float = 0.0,
                 block2_acceleration: float = 0.0,
                 block2_velocity: float = 0.0,
                 collision: bool = False,
                 collision_frame: int = None,
                 impuls: float = 0.0
                 ):
        self.__g_force = g_force
        self.__grade_force = grade_force
        self.__friction_force_still = friction_force_still
        self.__friction_force_moving = friction_force_moving
        self.__acceleration = acceleration
        self.__block2_acceleration = block2_acceleration
        self.__block2_velocity = block2_velocity
        self.__collision = collision
        self.__collision_frame = collision_frame
        self.__impuls = impuls

    @property
    def g_force(self):
        return self.__g_force

    @property
    def grade_force(self):
        return self.__grade_force

    @property
    def friction_force_still(self):
        return self.__friction_force_still

    @property
    def friction_force_moving(self):
        return self.__friction_force_moving

    @property
    def acceleration(self):
        return self.__acceleration

    @property
    def block2_acceleration(self):
        return self.__block2_acceleration

    @property
    def block2_velocity(self):
        return self.__block2_velocity

    @property
    def collision(self):
        return self.__collision

    @property
    def collision_frame(self):
        return self.__collision_frame

    @property
    def impuls(self):
        return self.__impuls

    @g_force.setter
    def g_force(self, value):
        self.__g_force = value

    @grade_force.setter
    def grade_force(self, value):
        self.__grade_force = value

    @friction_force_still.setter
    def friction_force_still(self, value):
        self.__friction_force_still = value

    @friction_force_moving.setter
    def friction_force_moving(self, value):
        self.__friction_force_moving = value

    @acceleration.setter
    def acceleration(self, value):
        self.__acceleration = value

    @collision.setter
    def collision(self, value):
        self.__collision = value

    @block2_acceleration.setter
    def block2_acceleration(self, value):
        self.__block2_acceleration = value

    @block2_velocity.setter
    def block2_velocity(self, value):
        self.__block2_velocity = value

    @collision_frame.setter
    def collision_frame(self, value):
        self.__collision_frame = value

    @impuls.setter
    def impuls(self, value):
        self.__impuls = value
