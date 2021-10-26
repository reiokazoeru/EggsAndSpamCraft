from math import *
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
            return signedDstRect(((self.pos),(self.size)),target)

def tupleSub(t1:tuple,t2:tuple):
    return (t1[0]-t2[0],t1[1]-t2[1])
def tupleAbs(t1:tuple):
    return (abs(t1[0]),abs(t1[1]))

def length(p1:tuple): #use pythagoras to find line length from point offest from (0,0)
    return sqrt(p1[0]*p1[0]+p1[1]*p1[1])
def lineLength(p1:tuple,p2:tuple): #use length function to calc distance from p1 to p2
    return length((p1[0]-p2[0],p1[1]-p2[1]))

def signedDstRect(rectPos,RectSize,target:tuple):
    offset = tupleAbs(tupleSub(target,rectPos))
    f = (RectSize[0]/2) #x size /2
    g = -1 * (RectSize[1]/2) #y size /2
    signedDst = sqrt(max(0,(offset[0]-f))*max(0,(offset[0]-f))+max(0,(offset[1]-g))*max(0,(offset[1]-g)))
    return signedDst
def signedDstCircle(p:tuple,center:tuple,radius:float):
    return lineLength(center,p)-radius
def signedDstFList(list,target:tuple):
    shortest = float('inf')
    for i in list:
        shortest = min(shortest,i.signedDst(target))
    return shortest            
def drawList(list:list,screen):
    for i in list:
        i.draw()
pygame.init()
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


mousePos = (0,0)

screenSize = (640,640)
screen = pygame.display.set_mode(screenSize)
runBool = True
#shape vars
idleShapeList= [Shape("circle",(120,420),30.0,BLUE),Shape("rectangle",(420,120),(20,10),RED)]
activeShapeList= [Shape("circle",mousePos,0)]
shapeList = [activeShapeList,idleShapeList]
while runBool:
    #event handler
    for event in pygame.event.get():
        if event.type == QUIT:
            runBool = False
        elif event.type == MOUSEMOTION:
            mousePos= event.pos
    #shape constructer and updater
    print(idleShapeList[1].type)
    sDst = signedDstFList(idleShapeList,mousePos)
    activeShapeList[0].pos = mousePos
    activeShapeList[0].size = sDst
    #screen drawer
    screen.fill((0,0,0))
    drawList(shapeList)
    pygame.display.update()
pygame.quit()