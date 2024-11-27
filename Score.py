import pygame

def displayScore(map, win):
    white = (255, 255, 255)
    black = (11,11,11)
    X = 1900
    Y = 40
    pygame.display.set_caption('Zombie Apocalypse')
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(str(map.score), True, white, black)
    textRect = text.get_rect()
    textRect.center = (X // 2, Y // 2)
    win.blit(text, textRect)