import pygame
from spriteClass import *

class Tile:
    def __init__(self, canWalkThrough, path, name):
        self.name = name
        self.height = 32
        self.width = 32
        self.image = pygame.transform.scale(pygame.image.load(path).convert(), (self.width, self.height))
        self.canWalkThrough = canWalkThrough

class LevelManager:
    def __init__(self):
        self.self = self
        self.currentLevel = LEVEL_1
        self.xTiles = 25
        self.yTiles = 22
        self.tileList = [Tile(True, "sprites/tilesets/grass.png", "Grass"),
                        Tile(True, "sprites/tilesets/stone.png", "Stone"),
                        Tile(False, "sprites/tilesets/stoneWall.png", "Stone Wall"),
                        Tile(True, "sprites/tilesets/water.png", "Water")]
    
    def drawLevel(self, window, level):
        for row in range(0, self.xTiles):
            for column in range(self.yTiles):
                if level[column][row] == 0:
                    window.blit(self.tileList[0].image, (row * self.tileList[0].width, column * self.tileList[0].height))
                elif level[column][row] == 1:
                    window.blit(self.tileList[1].image, (row * self.tileList[1].width, column * self.tileList[1].height))
                elif level[column][row] == 2:
                    window.blit(self.tileList[2].image, (row * self.tileList[2].width, column * self.tileList[2].height))
                elif level[column][row] == 3:
                    window.blit(self.tileList[3].image, (row * self.tileList[3].width, column * self.tileList[3].height))


LEVEL_1 = [[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
          [2, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
          [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
          [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
          [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
          [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
          [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
          [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
          [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
          [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 2],
          [2, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 1, 1, 1, 1, 0, 2],
          [2, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 1, 1, 1, 1, 0, 2],
          [2, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 1, 1, 0, 0, 2],
          [2, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
          [2, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
          [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
          [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
          [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
          [2, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
          [2, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 2],
          [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 2],
          [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]]