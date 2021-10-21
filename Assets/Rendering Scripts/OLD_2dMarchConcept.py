from math import *
import pygame
from pygame.draw import circle, rect
from pygame.locals import *
"""
so for given inital point (x,y) at angel r, calculate distance to all objects in scene,
then draw cirle (just for vis) and extend line at angle r for shortest distance
repeat until line length is less than given threshold
rectangle eq
"""
def tupleSub(t1:tuple,t2:tuple):
    return tuple(map(lambda i, j: i - j, t1, t2))
def tupleAbs(t1:tuple):
    return (abs(t1[0]),abs(t1[1]))

def length(p1:tuple): #use pythagoras to find line length from point offest from (0,0)
    return sqrt(p1[0]*p1[0]+p1[1]*p1[1])
def lineLength(p1:tuple,p2:tuple): #use length function to calc distance from p1 to p2
    return length((p1[0]-p2[0],p1[1]-p2[1]))

def signedDistanceToCircle(p:tuple,center:tuple,radius:float):
    return lineLength(center,p)-radius
def signedDistanceToRect(p:tuple,center:tuple,size:tuple):
    offset = tupleSub(tupleAbs(tupleSub(p,center)),size)
    unsignedDist = length(max(offset,(0,0)))
    dstInsideBox = max(min(offset,(0,0)))
    return unsignedDist + dstInsideBox


screenSize = ((640,240))
mousePos = (0,0)    
circleRadius = 0
testPos = (640/2,240/2)
testRadius = 20.0
pygame.init()
screen = pygame.display.set_mode(screenSize)
runBool = True
while runBool:
    for event in pygame.event.get():
        if event.type == QUIT:
            runBool = False
        elif event.type == MOUSEMOTION:
            mousePos= event.pos
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                testRadius +=5
            elif event.button == 3:
                testRadius -=5
    #vars to update on frame advance
    testRect = Rect(testPos[0]-testRadius/2,testPos[1]-testRadius/2,testRadius*2,testRadius*2)
    circleRadius = signedDistanceToRect(mousePos,testRect.center,(testRadius,testRadius))
    #items to put on screen
    screen.fill((0,0,0))
    pygame.draw.circle(screen,(255,255,255),mousePos,circleRadius)
    pygame.draw.rect(screen,(255,0,0),testRect)
    #pygame.draw.circle(screen,(255,0,0),testPos,testRadius)
    #update screen
    pygame.display.update()
pygame.quit()