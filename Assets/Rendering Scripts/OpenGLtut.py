from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

window = 0 # glut window number
width, height = 500, 400 # window size

def refresh2d(width,height):
    glViewport(0,0,width,height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0,width,0.0,height,0.0,1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
def drawRect(x,y,width,height): #draw a rectangle
    glBegin(GL_QUADS) #start drawing the rectangle
    glVertex2f(x,y) #bottom left point
    glVertex2f(x+width,y) #bottom right point
    glVertex2f(x+width,y+height) #top right point
    glVertex2f(x,y+height) #top left point
    glEnd() #done drawing rect

def draw():# ondraw is called all the time
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # clear the screen
    glLoadIdentity()# reset position
    refresh2d(width,height)

    glColor3f(0.0,0.0,1.0)
    drawRect(10,10,480,380)
   
    glutSwapBuffers()  # important for double buffering
   

# initialization
glutInit() # initialize glut
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_ALPHA | GLUT_DEPTH)
glutInitWindowSize(width, height)  # set window size
glutInitWindowPosition(0, 0) # set window position
window = glutCreateWindow("gex")# create window with title
glutDisplayFunc(draw)  # set draw function callback
glutIdleFunc(draw) # draw all the time
glutMainLoop()    