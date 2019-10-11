import pygame
from spriteClass import *

class Button:
    def __init__(self, xPos, yPos, width, height, color, text):
        self.xPos = xPos
        self.yPos = yPos
        self.width = width
        self.height = height
        self.color = color
        self.text = text
    
    def draw(self, window, outline = None):
        if outline:
            pygame.draw.rect(window, outline, (self.xPos - 2, self.yPos - 2, self.width+4, self.height + 4), 0)
            
        pygame.draw.rect(window, self.color, (self.xPos, self.yPos, self.width, self.height), 0)
        
        if self.text != '':
            font = pygame.font.SysFont('segoeuiblack', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            window.blit(text, (self.xPos + (self.width/2 - text.get_width()/2), self.yPos + (self.height/2 - text.get_height()/2)))

    def mouseIsHover(self, pos):
        if pos[0] > self.xPos and pos[0] < self.xPos + self.width:
            if pos[1] > self.yPos and pos[1] < self.yPos + self.height:
                return True
            
        return False

class MainMenu:
    def __init__(self, screenWidth, screenHeight):
        self.gameLogo = Sprite("")
        self.newGameButton = Button(screenWidth / 2, screenHeight /2, 250, 100, (255, 0, 0), "New Game")

    def update(self):
        #asd

    def draw(self, window):
        #asd
    
    def onClickNewGame():
        #asd
    
