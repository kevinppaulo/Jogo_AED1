# Importar módulo pygame e do sistema
import pygame
import sys
# Constantes usadas pelo pygame
from pygame.locals import *
from Directions import *
from Player import *
from Colors import *
from Config import *
from Backgrounds import *

import math


WINDOW_WIDTH = 920
WINDOW_HEIGHT = 540

backgroundImg = "assets/backgrounds/background_1.png"


def initPlayableCharacter():
    character = Player()
    character.setSpriteFile("assets/sprites/spritestripbw.png")
    character.setSpriteHeight(256)
    character.setSpriteWidth(256)
    character.setSpriteMaxWidth(256 * 6)
    character.setCurrentFrameState(1)
    character.setMaxFrameState(6)
    character.setPosx(5)
    character.setPosy(WINDOW_HEIGHT - character.getSpriteHeight() - 15)
    return character

def parallaxDifferential(zdepth):
    return (2 * 15 - zdepth)

def drawParallaxBackground(bg,canvas):
    dx = parallaxDifferential(bg.getZDepth())
    if(bg.getXCoord() != 0):
        canvas.blit(
            bg.getDrawable().subsurface(-bg.getXCoord(), 0 ,WINDOW_WIDTH + ( bg.getXCoord() ), WINDOW_HEIGHT), (0,0))

        canvas.blit(
            bg.getDrawable().subsurface(0, 0, WINDOW_WIDTH - (WINDOW_WIDTH + bg.getXCoord() ) , WINDOW_HEIGHT),(WINDOW_WIDTH + bg.getXCoord(), 0))

    else:
        canvas.blit(
            bg.getDrawable(), (0,0)
        )
   # canvas.blit(bg.getDrawable().subsurface(0, 0 ,WINDOW_WIDTH + ( bg.getXCoord() - dx), WINDOW_HEIGHT), (WINDOW_WIDTH + ( bg.getXCoord() - dx),0))


    #print("canvas.blit(bg.getDrawable().subsurface(0, 0 ,{}, {}), {},0))"
         # .format(WINDOW_WIDTH + ( bg.getXCoord() - dx),WINDOW_HEIGHT, (WINDOW_WIDTH - (WINDOW_WIDTH + ( bg.getXCoord() - dx)) )))

   # print("canvas.blit(bg.getDrawable().subsurface({}, 0 ,{},{}), (0,0))".format(-bg.getXCoord(),WINDOW_WIDTH + ( bg.getXCoord() - dx), WINDOW_HEIGHT))

    # (playableCharacter.getSpriteFile()).subsurface(
    #         playableCharacter.getFrameQuad())


def updateJump(character):
    jumpVelocity = 8
    characterMass = 2
    print("JUMP DETECTRD")

    if(jumpVelocity > 0):
        F = (0.5 * characterMass * (jumpVelocity * jumpVelocity))
    else:
        F = -(0.5 * characterMass * (jumpVelocity * jumpVelocity))
        character.getPosy(character.getPosy() - F)
        jumpVelocity -= 1

    if character.getPosy() >= 500:
        character.setPosy(500)
        character.move(Directions.IDLE)
        jumpVelocity = 8

def main():
    fpsClock = pygame.time.Clock()
    pygame.init()
    pygame.mixer.init()
    sounda = pygame.mixer.music.load("assets/soundtrack/bg.mp3")
    pygame.mixer.music.play(sounda)
    DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('Projeto AED')

    playableCharacter = initPlayableCharacter()
    backgroundImages = []

    #Total de 7
    for i in range(5, 0, -1):
        # if i == 2:
        #     continue
        backgroundImages.append(
            Backgrounds(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, "assets/backgrounds/iloveimg-resized/bw/{}.png".format(i), i))

    while True:
        DISPLAYSURF.fill(Colors.WHITE)
        # CAPTURA DE EVENTOS
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playableCharacter.move(Directions.LEFT)
                if event.key == pygame.K_RIGHT:
                    playableCharacter.move(Directions.RIGHT)
                if event.key == pygame.K_UP:
                    playableCharacter.move(Directions.UP)
            if event.type == pygame.KEYUP:
                playableCharacter.move(Directions.IDLE)

        # Lógica do jogo vai aqui
        # ------
        # set character position
        if (playableCharacter.getMovingDirection() == Directions.RIGHT):
            playableCharacter.setPosx(playableCharacter.getPosx() + 45)

        if (playableCharacter.getMovingDirection() == Directions.LEFT):
            playableCharacter.setPosx(playableCharacter.getPosx() - 45)

        if(playableCharacter.getMovingDirection() == Directions.UP):
            updateJump(playableCharacter)

        # Desenhar na Surface
        # Desenhar backgorund
        # backgroundImage = Backgrounds(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT, "assets/backgrounds/background_1.png")


        for image in backgroundImages:
            if(image == backgroundImages[2] or image == backgroundImages[1]):
                continue
            if(-image.getXCoord() + parallaxDifferential(image.getZDepth()) > WINDOW_WIDTH):
                image.setXCoord(0)
            else:
                image.setXCoord(image.getXCoord() - parallaxDifferential(image.getZDepth()))

            #image.setXCoord(image.getXCoord() - (math.log2(-(image.getZDepth()-4)+1)+5))
            #print(str(image.getZDepth() )+ " "+ str(image.getXCoord()))

        DISPLAYSURF.blit(backgroundImages[0].getDrawable(), (0,0))
        for i in range(1,len(backgroundImages)):
            drawParallaxBackground(backgroundImages[i], DISPLAYSURF)


        #DISPLAYSURF.fill(Colors.SPACE_GRAY)
        #DISPLAYSURF.blit(backgroundImage.getDrawable(), (0, 0))


        if (playableCharacter.getCurrentFrameState() > playableCharacter.getMaxFrameState() - 1):
            playableCharacter.setCurrentFrameState(1)
        else:
            playableCharacter.setCurrentFrameState(
                playableCharacter.getCurrentFrameState() + 1)

        #print(playableCharacter.getCurrentFrameState())

        charSprite = pygame.image.load(playableCharacter.getSpriteFile()).subsurface(
            playableCharacter.getFrameQuad())

        #print(playableCharacter.getFrameQuad())
        DISPLAYSURF.blit(
            charSprite, (playableCharacter.getPosx(), playableCharacter.getPosy()))

        drawParallaxBackground(backgroundImages[-1], DISPLAYSURF)
        drawParallaxBackground(backgroundImages[0], DISPLAYSURF)

        pygame.display.update()
        fpsClock.tick(FRAME_RATE)


main()
