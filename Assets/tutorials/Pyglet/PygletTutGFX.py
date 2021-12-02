import pyglet
from pyglet.gl import *
import math
import os

class MouseH:
    """
    a class for holding mouse info
    x: x pos
    y: y pos
    dx: x pos rel to last frame
    dy: y pos rel to last frame
    """
    def __init__(self,x,y,dx,dy,m=10) -> None:
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.m = m
        self.hx = x + dx*m
        self.hy = y + dy*m

class Triangle:
    """
    a def for a triangle 
    """
    def __init__(self,p1,p2,p3) -> None:
        self.p1 = p1
        self.p2 = p2 
        self.p3 = p3
    
    def signDst(pG,self):
        pass
        """
        make plane from tri
        offset point relative to plane 
        
        """
#fix root dir
path = os.path.abspath(os.path.join('..', os.getcwd()))
pyglet.resource.path = [path] 
pyglet.resource.reindex()

#make window
width =720
height = 480
title = 'GEX'

window = pyglet.window.Window(width,height,title)
window.projection = pyglet.window.Projection3D()
batch = pyglet.graphics.Batch()



@window.event
def on_draw():
    window.clear()
    batch.draw()

@window.event
def on_mouse_drag(x,y,dx,dy,buttons,modifiers):
    glRotatef(1,dx,dy,0)

def rotate(dt):
    glRotatef(0.5,dt,dt,dt)

if __name__ == "__main__":
    glEnable(GL_MULTISAMPLE_ARB)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)

    #model = pyglet.model.load("logo3d.obj",batch=batch)
    glTranslatef(0,0,-3)
    pyglet.clock.schedule_interval(rotate,1/60)
    pyglet.app.run()