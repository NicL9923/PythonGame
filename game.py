import pygame
from sys import exit
from pygame.locals import *

from characterClasses import *
from gameObjectClass import *
from uiClasses import *
from levelClass import *


pygame.init()

#Global game/window variables
running = True
onMenu = True
screenWidth = 800
screenHeight = 700
font = pygame.font.SysFont('segoeuiblack', 30)
itemsFound = 0

#Window creation
window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Aiden's World")
windowIcon = pygame.image.load("sprites/Icon.png")
pygame.display.set_icon(windowIcon)
gameClock = pygame.time.Clock()



#Object creation/handling
player = PlayerCharacter(250, 250, 3, 100, "sprites/characters/AidenSpiderman.png")
bullets = []

#Sprite handling
spriteList = pygame.sprite.Group()
background = Sprite("sprites/Background.png")

spriteList.add(background)
spriteList.add(player.sprite)

#Audio handling
#sound = pygame.mixer.Sound("fileName")
#sound.play()

#music = pygame.mixer.music.load("fileName")
#pygame.mixer.music.play(-1 to loop)


#Main Menu Loop
while onMenu:

        mainMenu = MainMenu(screenWidth, screenHeight)

        print(int(gameClock.get_fps()))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                onMenu = False
                running = False
        
        mousePos = pygame.mouse.get_pos()
        mouseClick = pygame.mouse.get_pressed()


        if not mainMenu.update(mousePos, mouseClick):
            onMenu = False

        mainMenu.draw(window)
        pygame.display.update()

        gameClock.tick(60)


#Game's Main Loop
while running:

    print(int(gameClock.get_fps()))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Bullet/Projectile updating
    for bullet in bullets:
        if bullet.xPos < 800 and bullet.xPos > 0:
            if (bullet.direction == "right"):
                bullet.xPos += bullet.speed
            if (bullet.direction == "left"):
                bullet.xPos -= bullet.speed
            if (bullet.direction == "up"):
                bullet.yPos -= bullet.speed
            if (bullet.direction == "down"):
                bullet.yPos += bullet.speed
        else:
            bullets.pop(bullets.index(bullet))

    #Input Management (Possibly moved to class InputManager later)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if len(bullets) < 20:
            bullets.append(Projectile(player.xPos, player.yPos, 10, player.facing, 2, (0, 0, 0)))


    if keys[pygame.K_w] and player.yPos > player.speed:
        player.yPos -= player.speed
        player.facing = "up"
        itemsFound += 1
    elif keys[pygame.K_s] and player.yPos < screenHeight - 25:
        player.yPos += player.speed
        player.facing = "down"
    if keys[pygame.K_a] and player.xPos > player.speed:
        player.xPos -= player.speed
        player.facing = "left"
    elif keys[pygame.K_d] and player.xPos < screenWidth - 25:
        player.xPos += player.speed
        player.facing = "right"

    #Update stuff
    player.update()

    #Rendering stuff
    spriteList.draw(window)

    for bullet in bullets:
        bullet.draw(window)

    #pygame.draw.rect(window, (255, 0, 0), player.hitbox, 2)

    text = font.render("Items found: " + str(itemsFound), 1, (0, 128, 128))
    window.blit(text, (10, 10))

    pygame.display.update()


    gameClock.tick(60)

pygame.quit()
exit()