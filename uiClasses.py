import pygame
from sys import exit
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
            font = pygame.font.SysFont('segoeuiblack', 40)
            text = font.render(self.text, 1, (0, 0, 0))
            window.blit(text, (self.xPos + (self.width/2 - text.get_width()/2), self.yPos + (self.height/2 - text.get_height()/2)))

    def mouseIsHover(self, pos):
        if pos[0] > self.xPos and pos[0] < self.xPos + self.width:
            if pos[1] > self.yPos and pos[1] < self.yPos + self.height:
                return True
            
        return False

class MainMenu:
    def __init__(self, screenWidth, screenHeight):
        self.gameLogo = pygame.image.load("sprites/Logo.png")
        self.background = pygame.image.load("sprites/MainMenuBG.png")
        self.newGameButton = Button(screenWidth / 2 - 125, 250, 250, 100, (255, 0, 0), "New Game")
        self.loadGameButton = Button(screenWidth / 2 - 125, 400, 250, 100, (0, 255, 0), "Load Game")
        self.exitGameButton = Button(screenWidth / 2 - 125, 550, 250, 100, (0, 0, 255), "Exit Game")

    def update(self, mousePos, mouseClick):
        #if mouse within sprites, display a separate, brighter sprite?
        if self.newGameButton.mouseIsHover(mousePos):
            print("Hovering over New Game button")
            if mouseClick[0] == 1:
                return self.onClickNewGame()
        if self.loadGameButton.mouseIsHover(mousePos):
            if mouseClick[0] == 1:
                return self.onClickLoadGame()
        if self.exitGameButton.mouseIsHover(mousePos):
            if mouseClick[0] == 1:
                return self.onClickExitGame()
        return True


    def draw(self, window):
        window.fill((255, 255, 255))
        window.blit(self.background, (0, 0))
        window.blit(self.gameLogo, (100, 10))
        self.newGameButton.draw(window)
        self.loadGameButton.draw(window)
        self.exitGameButton.draw(window)
    
    def onClickNewGame(self):
        return False
    
    def onClickLoadGame(self):
        return False

    def onClickExitGame(self):
        pygame.quit()
        exit()
        return False