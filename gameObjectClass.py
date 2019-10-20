import pygame
from spriteClass import *

class GameObject:
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos

class Projectile(GameObject):
    def __init__(self, xPos, yPos, speed, direction, radius, color):
        super().__init__(xPos, yPos)
        self.speed = speed
        self.direction = direction
        self.radius = radius
        self.color = color

    def draw(self, window):
        pygame.draw.circle(window, self.color, (self.xPos, self.yPos), self.radius)

class Collectible(GameObject):
    def __init__(self, xPos, yPos):
        super().__init__(xPos, yPos)
        self.sprite = Sprite("sprites/items/Pumpkin.png")
