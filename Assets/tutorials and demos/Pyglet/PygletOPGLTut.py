import pyglet
from pyglet.gl import *
# direct OpenGL commands to this window
window = pyglet.window.Window()

cubeVerts = [
    (0,0,0),
    (1,0,0),
    (1,1,0),
    (0,1,0),
    (0,0,1),
    (1,0,1),
    (1,1,1),
    (0,1,1)
]

@window.event
def on_draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glBegin(GL_TRIANGLES)
    glVertex2f(0,0)
    glVertex2f(window.width,0)
    glVertex2f(window.width,window.height)
    glEnd()

pyglet.app.run()