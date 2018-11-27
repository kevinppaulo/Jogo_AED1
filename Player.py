from Directions import *
from GenericCharacter import *


class Player(GenericCharacter):

    def __init__(self):
        super().__init__()
        self.weapons = []
        self.currentWeapon = None

        # ACTION STATES
        self.__MOVING_LEFT = False
        self.__MOVING_RIGHT = False
        self.__JUMPING = False
        self.__PRONING = False
        self.__IDLE = False

    def move(self, direction):
        if (direction == Directions.LEFT):
            self.__MOVING_LEFT = True
            self.__MOVING_RIGHT = False
            self.__JUMPING = False
            self.__PRONING = False
            self.__IDLE = False

        elif (direction == Directions.RIGHT):
            self.__MOVING_LEFT = False
            self.__MOVING_RIGHT = True
            self.__JUMPING = False
            self.__PRONING = False
            self.__IDLE = False

        elif (direction == Directions.UP):
            self.__MOVING_LEFT = False
            self.__MOVING_RIGHT = False
            self.__JUMPING = True
            self.__PRONING = False
            self.__IDLE = False

        elif (direction == Directions.DOWN):
            self.__MOVING_LEFT = False
            self.__MOVING_RIGHT = False
            self.__JUMPING = False
            self.__PRONING = True
            self.__IDLE = False

        if (direction == Directions.IDLE):
            self.__MOVING_LEFT = False
            self.__MOVING_RIGHT = False
            self.__JUMPING = False
            self.__PRONING = False
            self.__IDLE = True

    def getMovingDirection(self):
        if (self.__MOVING_LEFT):
            return Directions.LEFT
        elif (self.__MOVING_RIGHT):
            return Directions.RIGHT
