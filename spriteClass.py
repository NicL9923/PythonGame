import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, path, scaleX=None, scaleY=None):
        super().__init__()
        self.imgLocation = path
        self.image = pygame.image.load(path).convert_alpha()
        #self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        if scaleX and scaleY:
            self.image = pygame.transform.scale(self.image, (scaleX, scaleY))
            self.rect = self.image.get_rect()