#Tiles ->
#Level design by matrices where in each coord specifies the tile present 
    #Ex: [ stone, wood, dirt
    #        stone, dirt, wood  ]

#Implement collisions on a per tile basis? (Can walk through water and floors but not walls)


#Next TODOs: flesh out main menu buttons, level editor/tiles, actual game objective (Ex: collecting items), sprites/animations, music on or off button

from spriteClass import *

class Tile:
    def __init__(self, canWalkThrough, path):
        self.sprite = Sprite(path)
        self.canWalkThrough = canWalkThrough

class Level:
    def __init__(self):
        self.self = self
        #self.tiles = [Tile(x), Tile(y), etc]?

Level1 = [".........................",
          ".........................",
          ".........................",
          ".........................",
          ".........................",
          ".........................",
          ".........................",
          ".........................",
          ".........................",
          ".........................",
          ".........................",
          ".........................",
          ".........................",
          ".........................",
          ".........................",
          ".........................",
          ".........................",
          ".........................",
          ".........................",
          ".........................",
          ".........................",
          "........................."]