import pygame
from pygame.locals import *
"""
so for given inital point (x,y) at angel r, calculate distance to all objects in scene,
then draw cirle (just for vis) and extend line at angle r for shortest distance





"""



screenSize = ((640,240))

pygame.init()
screen = pygame.display.set_mode(screenSize)
runBool = True
while runBool:
    for event in pygame.event.get():
        if event.type == QUIT:
            runBool = False
    #items to put on screen
    #update screen
    pygame.display.update()
pygame.quit()