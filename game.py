import pygame
from pygame.locals import *
pygame.init()

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Aiden's World")

running = True

x = 250
y = 250
xVel = 5
yVel = 5


while running:

    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False

        window.fill((0, 0, 0))

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            print("W")
            y -= yVel
        if keys[pygame.K_a]:
            print("A")
            x -= xVel
        if keys[pygame.K_s]:
            print("S")
            y += yVel
        if keys[pygame.K_d]:
            print("D")
            x += xVel

    screen_clamp()

    pygame.draw.rect(window, (0, 0, 255), (x, y, 25, 25))


    pygame.display.update()

pygame.quit()


def screen_clamp():
    if x > 500:
        x = 500
    if x < 0:
        x = 0
    
    if y > 500:
        y = 500
    if y < 0:
        y = 0
    return