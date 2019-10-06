import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, path):
        super().__init__()
        self.imgLocation = path
        self.image = pygame.image.load(path).convert()
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()