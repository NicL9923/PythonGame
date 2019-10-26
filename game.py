import pygame
import random
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
screenHeight = 704
font = pygame.font.SysFont('segoeuiblack', 30)
itemsFound = 0

#Window creation
window = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Aiden's World")
windowIcon = pygame.image.load("sprites/Icon.png").convert_alpha()
pygame.display.set_icon(windowIcon)
gameClock = pygame.time.Clock()
random.seed()



#Object creation/handling
levelManager = LevelManager()
player = PlayerCharacter(250, 250, 3, 100, "sprites/characters/AidenSpiderman.png")
pumpkinCollectibles = []
for i in range(15):
    pumpkinCollectibles.append(Collectible(random.randint(1, 799), random.randint(1, 704)))

bullets = []

#Sprite handling
spriteList = pygame.sprite.Group()

spriteList.add(player.sprite)
for pumpkin in pumpkinCollectibles:
    pumpkin.sprite.rect.x = pumpkin.xPos
    pumpkin.sprite.rect.y = pumpkin.yPos
    spriteList.add(pumpkin.sprite)

#Audio handling
#sound = pygame.mixer.Sound("fileName")
#sound.play()

music = pygame.mixer.music.load("audio/music/Explore1.wav")
pygame.mixer.music.play(-1)


#Main Menu Loop
def mainMenu():
    global onMenu
    global running

    onMenu = True
    
    while onMenu:

            mainMenu = MainMenu(screenWidth)

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


music = pygame.mixer.music.load("audio/music/Wonder1.wav")
pygame.mixer.music.play(-1)

mainMenu()

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

    #Collectibles check
    for pumpkin in pumpkinCollectibles:
        if player.xPos >= pumpkin.xPos - 16 and player.xPos <= pumpkin.xPos + 16:
            if player.yPos >= pumpkin.yPos - 16 and player.yPos <= pumpkin.yPos + 16:
                itemsFound += 1
                pumpkin.sprite.kill()
                pumpkinCollectibles.pop(pumpkinCollectibles.index(pumpkin))

    if itemsFound == 15:
        itemsFound = 0
        mainMenu()

    #Input Management (Possibly moved to class InputManager later)
    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        if len(bullets) < 20:
            bullets.append(Projectile(player.xPos, player.yPos, 10, player.facing, 2, (0, 0, 0)))


    if keys[pygame.K_w] and player.yPos > player.speed:
        player.yPos -= player.speed
        player.facing = "up"
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
    levelManager.drawLevel(window, LEVEL_1)
    spriteList.draw(window)

    for bullet in bullets:
        bullet.draw(window)

    #pygame.draw.rect(window, (255, 0, 0), player.hitbox, 2)

    text = font.render("Items found: " + str(itemsFound), 1, (255, 45, 45))
    window.blit(text, (10, 10))

    pygame.display.update()


    gameClock.tick(60)

pygame.quit()
exit()