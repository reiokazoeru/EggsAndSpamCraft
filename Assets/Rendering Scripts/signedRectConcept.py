from math import *
import pygame
from pygame.draw import rect
from pygame.locals import *

def tupleSub(t1:tuple,t2:tuple):
    return (t1[0]-t2[0],t1[1]-t2[1])
def tupleAbs(t1:tuple):
    return (abs(t1[0]),abs(t1[1]))

def length(p1:tuple): #use pythagoras to find line length from point offest from (0,0)
    return sqrt(p1[0]*p1[0]+p1[1]*p1[1])
def lineLength(p1:tuple,p2:tuple): #use length function to calc distance from p1 to p2
    return length((p1[0]-p2[0],p1[1]-p2[1]))

def goodSignedDistanceToRect(rect:Rect,target:tuple):
    offset = tupleAbs(tupleSub(target,rect.center))
    f = (rect.right-rect.centerx) #x size /2
    g = -1 * (rect.top-rect.centery) #y size /2
    signedDst = sqrt(max(0,(offset[0]-f))*max(0,(offset[0]-f))+max(0,(offset[1]-g))*max(0,(offset[1]-g)))
    return signedDst
pygame.init()
screenSize = (640,240)
screen = pygame.display.set_mode(screenSize)
testSize = (320,120)
testPos = ((screenSize[0]/2 - testSize[0]/2),(screenSize[1]/2 - testSize[1]/2)) # centers
testRect = Rect(testPos[0],testPos[1],testSize[0],testSize[1])
caption = "null"
runBool = True
mousePos = (0,0)
while runBool:
    for event in pygame.event.get():
        if event.type == QUIT:
            runBool = False
        elif event.type == MOUSEMOTION:
            mousePos= event.pos
            caption = str(lineLength(testRect.center,mousePos))
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(255,0,0),testRect)
    pygame.draw.circle(screen,(255,255,255),mousePos,goodSignedDistanceToRect(testRect,mousePos))
    pygame.display.set_caption(str(goodSignedDistanceToRect(testRect,mousePos)))
    pygame.display.update()
pygame.quit()