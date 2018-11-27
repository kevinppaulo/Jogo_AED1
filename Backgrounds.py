import pygame
import sys
from pygame.locals import *
from Directions import *
from Colors import *
from Config import *


class Backgrounds:
    def __init__(self, xCoord=0, yCoord=0, backgroundWidth=0, backgroundHeight=0, backgroundImage=None, zdepth=1):
        self.__xCoord = xCoord
        self.__yCoord = yCoord
        self.__backgroundWidth = backgroundWidth
        self.__backgroundHeight = backgroundHeight
        self.__backgroundImage = backgroundImage
        self.__zdepth = zdepth


    def getDrawable(self):
        return pygame.image.load(self.__backgroundImage)


    def draw(self, canvas):
        canvas.fill(Colors.SPACE_GRAY)
        canvas.blit(self.getDrawable(), (self.__xCoord, self.__yCoord))

    def setXCoord(self, xCoord):
        self.__xCoord = xCoord

    def setYCoord(self, yCoord):
        self.__yCoord = yCoord

    def setZDepth(self, zdepth):
        self.__zdepth = zdepth

    def getXCoord(self):
        return self.__xCoord

    def getYCoord(self):
        return self.__yCoord

    def getZDepth(self):
        return self.__zdepth

    def getImageSrc(self):
        return self.__backgroundImage
