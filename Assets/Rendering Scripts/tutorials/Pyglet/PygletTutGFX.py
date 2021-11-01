from ctypes import DllCanUnloadNow
import pyglet
from pyglet.gl.gl import GL_POINTS

import os


#fix root dir
path = os.path.abspath(os.path.join('..', os.getcwd()))

pyglet.resource.path = [path] 
pyglet.resource.reindex()

#make window
window = pyglet.window.Window()

#game classes
class MouseH:
    """
    a class for holding mouse info
    x: x pos
    y: y pos
    dx: x pos rel to last frame
    dy: y pos rel to last frame
    """
    def __init__(self,x,y,dx,dy,m=100) -> None:
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.hx = x + dx*m
        self.hy = y + dy*m
#game vars 
mouseInfo = MouseH(0,0,0,0)
@window.event
def on_mouse_motion(x,y,dx,dy):
    mouseInfo = (x,y,dx,dy)
    print('mouse upd')
    print(str(mouseInfo))

@window.event
def on_draw():
    window.clear()
    print('scr upd')
    print(str(mouseInfo.x))
    pyglet.graphics.draw(2, pyglet.gl.GL_LINES,
        ('v2i', (100,100,0,0))
    )

pyglet.app.run()