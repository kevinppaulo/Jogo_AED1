import os
import sys


class GenericCharacter:
    def __init__(self, life=100, posx=1, posy=1, spriteFile=None, spriteWidth=1, spriteHeight=1, spriteMaxWidth=1,
                 currentFrameState=1, maxFrameState=1):
        self.setLife(life)
        self.setPosx(posx)
        self.setPosy(posy)
        self.setSpriteFile(spriteFile)
        self.setCurrentFrameState(currentFrameState)
        self.setSpriteWidth(spriteWidth)
        self.setSpriteHeight(spriteHeight)
        self.setSpriteMaxWidth(spriteMaxWidth)
        self.setMaxFrameState(maxFrameState)

    def setLife(self, life):
        self.__life = life

    def setPosx(self, posx):
        self.__posx = posx

    def setPosy(self, posy):
        self.__posy = posy

    def setSpriteFile(self, spriteFile):
        self.__spriteFile = spriteFile

    def setSpriteWidth(self, spriteWidth):
        self.__spriteWidth = spriteWidth

    def setSpriteMaxWidth(self, spriteMaxWidth):
        self.__spriteMaxWidth = spriteMaxWidth

    def setSpriteHeight(self, spriteHeight):
        self.__spriteHeight = spriteHeight

    def setCurrentFrameState(self, currentFrameState):
        self.__currentFrameState = currentFrameState

    def setMaxFrameState(self, maxFrameState):
        self.__maxFrameState = maxFrameState

    def getLife(self):
        return self.__life

    def getPosx(self):
        return self.__posx

    def getPosy(self):
        return self.__posy

    def getSpriteFile(self):
        return self.__spriteFile

    def getSpriteWidth(self):
        return self.__spriteWidth

    def getSpriteHeight(self):
        return self.__spriteHeight

    def getMaxFrameState(self):
        return self.__maxFrameState

    def getSpriteMaxWidth(self):
        return self.__spriteMaxWidth

    def getCurrentFrameState(self):
        return self.__currentFrameState

    def getFrameQuad(self):
        return (self.getSpriteWidth() * (self.getCurrentFrameState() - 1),
                0,
                self.getSpriteWidth(), self.getSpriteHeight()
                )
