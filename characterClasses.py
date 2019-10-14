import pygame
from spriteClass import *

class Character:

    def __init__(self, startX = 0, startY = 0, speed = 2, health = 100, spritePath = ""):
        self.xPos = startX
        self.yPos = startY
        self.speed = speed
        self.sprite = Sprite(spritePath)
        self.facing = "right"
        self.hitbox = (self.xPos, self.yPos, 32, 32)
        self.health = health

    def update(self):
        self.sprite.rect.x = self.xPos
        self.sprite.rect.y = self.yPos
        self.hitbox = (self.xPos, self.yPos, 32, 32)

    def hit(self):
        print("Character collision")

    def setXPos(self, xPos):
        self.xPos = xPos
    def getXPos(self):
        return self.xPos
    
    def setYPos(self, yPos):
        self.yPos = yPos
    def getYPos(self):
        return self.yPos
    
    def setSpeed(self, speed):
        self.speed = speed
    def getSpeed(self):
        return self.speed

    def setSprite(self, spritePath):
        self.sprite = Sprite(spritePath)
    def getSpritePath(self):
        return self.sprite.imgLocation

    

class PlayerCharacter(Character):
    def __init__(self, startX, startY, speed, health, spritePath):
        super().__init__(startX, startY, speed, health, spritePath)


class FriendlyCharacter(Character):
    def __init__(self, startX, startY, speed, health, spritePath):
        super().__init__(startX, startY, speed, health, spritePath)


class EnemyCharacter(Character):
    def __init__(self, startX, startY, speed, health, spritePath):
        super().__init__(startX, startY, speed, health, spritePath)
