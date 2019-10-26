import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, path, scaleSize=None):
        super().__init__()
        self.imgLocation = path
        self.image = pygame.image.load(path).convert_alpha()
        #self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        if scaleSize:
            self.image = pygame.transform.scale(self.image, scaleSize)
            self.rect = self.image.get_rect()