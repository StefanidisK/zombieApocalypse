# import modules
import pygame
pygame.display.init()
pygame.font.init()
import sys
import Score

# import classes
import Map
import Rock
import Test

# initialize display and map
grid = Map.Map()
win = grid.createMap()

# Make Objects
Rock.make(grid)
Test.make(grid)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # move objects and draw map
    for i in range (0, grid.mapSize):
        for j in range (0, grid.mapSize):
            grid.map[i][j].move(grid)
            win.blit(grid.map[i][j].image, (i*grid.picSize, j * grid.picSize))

    # reset all the move flags
    for i in range (0, grid.mapSize):
        for j in range (0, grid.mapSize):
            grid.map[i][j].isMoved = False

    # display text
    Score.displayScore(grid, win)

    pygame.display.update()
