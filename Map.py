import pygame
import Background

class Map():
    def __init__(self):
        self.map = []
        self.mapSize = 12
        self.picSize = 50
        self.score = 100

    def createMap(self):
        for i in range(0,self.mapSize):
            temp = []
            for j in range(0,self.mapSize):
                backgroundTile = Background.Background(self.picSize)
                temp.append(backgroundTile) # background
            self.map.append(temp)
        return pygame.display.set_mode(((self.mapSize * self.picSize)+400, self.mapSize * self.picSize))

