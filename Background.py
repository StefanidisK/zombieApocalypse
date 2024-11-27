import pygame

class Background():
    def __init__(self, picSize):
        self.image = pygame.image.load("background.png")
        self.image = pygame.transform.scale(self.image, (picSize, picSize))

    def move(self, map):
        return map, []