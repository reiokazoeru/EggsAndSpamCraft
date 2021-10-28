from math import *
from typing import List
import pygame
from pygame.draw import circle
from pygame.locals import *
class Shape():
    #a general shape class to make life easier when dealing with many @ once
    def __init__(self,type:str,pos:tuple,size,color=(255,255,255)) -> None:
        self.type = type
        self.pos = pos
        self.size = size
        self.color = color
    def draw(self,screen): #draw the shape to the screen
        if self.type == "circle":
            pygame.draw.circle(screen,self.color,self.pos,self.size)
        elif self.type == "rectangle":
            pygame.draw.rect(screen,self.color,(self.pos,self.size))
    def signedDst(self,target:tuple):
        if self.type == "circle":
            return signedDstCircle(target,self.pos,self.size)
        elif self.type == "rectangle":
            return signedDstRect((self.pos),(self.size),target)


def tupleSub(t1:tuple,t2:tuple):
    return (t1[0]-t2[0],t1[1]-t2[1])
def tupleAbs(t1:tuple):
    return (abs(t1[0]),abs(t1[1]))


def length(p1:tuple): #use pythagoras to find line length from point offest from (0,0)
    return sqrt(p1[0]*p1[0]+p1[1]*p1[1])
def lineLength(p1:tuple,p2:tuple): #use length function to calc distance from p1 to p2
    return length((p1[0]-p2[0],p1[1]-p2[1]))

def signedDstRect(rectPos,rectSize,target:tuple): #gen the signed distance to a rectangle while not on angle
    offset = tupleAbs(tupleSub(target,(rectPos[0]+rectSize[0]/2,rectPos[1]+rectSize[1]/2)))
    f = (rectSize[0]/2) #x size /2
    g = -1* (rectSize[1]/2) #y size /2
    signedDst = sqrt(max(0,(offset[0]-f))*max(0,(offset[0]-f))+max(0,(offset[1]+g))*max(0,(offset[1]+g)))
    return signedDst
def signedDstCircle(p:tuple,center:tuple,radius:float):
    return lineLength(center,p)-radius
def signedDstFList(list,target:tuple):
    shortest = float('inf')
    for i in list:
        shortest = min(shortest,i.signedDst(target))
    return shortest            
def drawList(list:list,screen):
    for l in list:
        for i in l:
            i.draw(screen)



pygame.init()
#colour constants
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
#mousePosInit
mousePos = (0,0)
#pre runtime stuff
screenSize = (640,640)
screen = pygame.display.set_mode(screenSize)
runBool = True
#idle shape vars
testCircle = Shape("circle",(120,420),30.0,BLUE)
testRect = Shape("rectangle",(420,120),(80,80),RED)
testRect1 = Shape("rectangle",(320,320),(80,80),RED)
#shape lists
idleShapeList= list()
idleShapeList.append(testCircle)
idleShapeList.append(testRect)
idleShapeList.append(testRect1)
#activeShapeVars
activeShapeList= [Shape("circle",mousePos,0)]
#main shape list
shapeList = [activeShapeList,idleShapeList]
#runtime
while runBool:
    #event handler
    for event in pygame.event.get():
        if event.type == QUIT:
            runBool = False
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                idleShapeList.append(Shape("rectangle",mousePos,(80,80),RED))
            elif event.button == 3:
                idleShapeList.append(Shape("circle",mousePos,30.0,BLUE))
        elif event.type == MOUSEMOTION:
            mousePos= event.pos
    #shape constructer and updater
    sDst = signedDstFList(idleShapeList,mousePos)
    activeShapeList[0].pos = mousePos
    activeShapeList[0].size = sDst
    #screen updater
    screen.fill((0,0,0)) #add background to buffer
    drawList(shapeList,screen) #add all shapes to buffer
    pygame.display.update() #draw buffer
pygame.quit()