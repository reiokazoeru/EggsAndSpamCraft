from math import *
import pygame
from pygame.draw import circle
from pygame.locals import *
"""
so for given inital point (x,y) at angel r, calculate distance to all objects in scene,
then draw cirle (just for vis) and extend line at angle r for shortest distance
repeat until line length is less than given threshold
rectangle eq
"""


def length(p1): #use pythagoras to find line length from point offest from (0,0)
    return sqrt(p1[0]*p1[0]+p1[1]*p1[1])
def lineLength(p1,p2): #use length function to calc distance from p1 to p2
    return length((p1[0]-p2[0],p1[1]-p2[1]))

def signedDistanceToCircle(p,center,radius:float):
    return length(center-p)-radius
def signedDistanceToRect(p,center,size):
    offset = abs(p-center) - size
    unsignedDist = length(max(offset,0))
    dstInsideBox = max(min(offset,0))
    return unsignedDist + dstInsideBox


screenSize = ((640,240))
mousePos = (0,0)
circleRadius = 0
testCirclePos = (640/2,240/2)
testCircleRadius = 5.0
pygame.init()
screen = pygame.display.set_mode(screenSize)
runBool = True
while runBool:
    for event in pygame.event.get():
        if event.type == QUIT:
            runBool = False
        elif event.type == MOUSEMOTION:
            mousePos= event.pos
            circleRadius = signedDistanceToCircle(mousePos,testCirclePos,testCircleRadius)
    #items to put on screen
    screen.fill((0,0,0))
    pygame.draw.circle(screen,(255,255,255),mousePos,circleRadius)
    pygame.draw.circle(screen,(255,0,0),testCirclePos,testCircleRadius)
    #update screen
    pygame.display.update()
pygame.quit()