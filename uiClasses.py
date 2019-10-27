import pygame
from sys import exit
from spriteClass import *

class Button:
    def __init__(self, xPos, yPos, imgPath, hoverImagePath):
        self.xPos = xPos
        self.yPos = yPos
        self.image = pygame.image.load(imgPath).convert_alpha()
        self.hoverImage = pygame.image.load(hoverImagePath).convert_alpha()
        self.width = self.image.get_size()[0]
        self.height = self.image.get_size()[1]
        self.isHover = False
    
    def draw(self, window):
        if self.isHover:
            window.blit(self.hoverImage, (self.xPos, self.yPos))
        else:
            window.blit(self.image, (self.xPos, self.yPos))

    def mouseIsHover(self, mousePos):
        if mousePos[0] > self.xPos and mousePos[0] < self.xPos + self.width:
            if mousePos[1] > self.yPos and mousePos[1] < self.yPos + self.height:
                return True
        return False

class MainMenu:
    def __init__(self, screenWidth):
        self.gameLogo = pygame.image.load("sprites/Logo.png").convert_alpha()
        self.background = pygame.transform.scale(pygame.image.load("sprites/MainMenuBG.png").convert_alpha(), (800, 704))
        self.newGameButton = Button(screenWidth / 2 - 125, 250, "sprites/ui/NewGameButton.png", "sprites/ui/NewGameButtonHover.png")
        self.loadGameButton = Button(screenWidth / 2 - 125, 400, "sprites/ui/LoadGameButton.png", "sprites/ui/LoadGameButtonHover.png")
        self.exitGameButton = Button(screenWidth / 2 - 125, 550, "sprites/ui/ExitGameButton.png", "sprites/ui/ExitGameButtonHover.png")

    def update(self, mousePos, mouseClick):
        if self.newGameButton.mouseIsHover(mousePos):
            self.newGameButton.isHover = True
            if mouseClick[0] == 1:
                return self.onClickNewGame()
        else:
            self.newGameButton.isHover = False
        if self.loadGameButton.mouseIsHover(mousePos):
            self.loadGameButton.isHover = True
            if mouseClick[0] == 1:
                return self.onClickLoadGame()
        else:
            self.loadGameButton.isHover = False
        if self.exitGameButton.mouseIsHover(mousePos):
            self.exitGameButton.isHover = True
            if mouseClick[0] == 1:
                return self.onClickExitGame()
        else:
            self.exitGameButton.isHover = False
        return True


    def draw(self, window):
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