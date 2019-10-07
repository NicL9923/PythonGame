import pygame
from sys import exit
from pygame.locals import *

from characterClasses import *
from gameObjectClass import *


pygame.init()


#Global game/window variables
running = True
screenWidth = 800
screenHeight = 700

#Window creation
window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Aiden's World")
windowIcon = pygame.image.load("sprites/Icon.png")
pygame.display.set_icon(windowIcon)
gameClock = pygame.time.Clock()



#Object creation/handling
player = PlayerCharacter(250, 250, 3, "sprites/characters/AidenSpiderman.png")


#Sprite handling
spriteList = pygame.sprite.Group()
background = Sprite("sprites/Background.png")

spriteList.add(background)
spriteList.add(player.sprite)



#Game's main loop
while running:

    print(int(gameClock.get_fps()))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Input Management (Possibly moved to class InputManager later)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w] and player.yPos > player.speed:
            player.yPos -= player.speed
        elif keys[pygame.K_s] and player.yPos < screenHeight - 25:
            player.yPos += player.speed
        if keys[pygame.K_a] and player.xPos > player.speed:
            player.xPos -= player.speed
        elif keys[pygame.K_d] and player.xPos < screenWidth - 25:
            player.xPos += player.speed

    #Update stuff
    player.update()

    #Rendering stuff
    spriteList.draw(window)
    pygame.display.update()

    gameClock.tick(60)


pygame.quit()
exit()