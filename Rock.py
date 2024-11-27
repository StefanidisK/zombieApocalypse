# import modules
import pygame
import Background
import random
import Test

# import objects
import Object

class Rock(Object.Object):
    def __init__(self, x, y, picSize):
        super().__init__(x, y)
        self.image = pygame.image.load("rock.png")
        self.image = pygame.transform.scale(self.image, (picSize, picSize))

    def move(self, map):
        self.moveRight(map)

    def moveRight(self, map):
        background = Background.Background(map.picSize)
        if self.x < 11 and not self.isMoved:
            if type(map.map[self.x + 1][self.y]) != Test.Test:
                map.map[self.x][self.y] = background
                self.x = self.x + 1
                map.map[self.x][self.y] = self
                self.isMoved = True
        return map

def make(map):
    for i in range(1, 11):
        tempX = random.randint(0, map.mapSize - 1)
        tempY = random.randint(0, map.mapSize - 1)
        rock = Rock(tempX, tempY, map.picSize)
        map.map[tempX][tempY] = rock
