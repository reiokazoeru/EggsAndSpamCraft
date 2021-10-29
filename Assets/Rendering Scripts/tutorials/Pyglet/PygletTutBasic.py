import pyglet
from pyglet import window as w
from pyglet.window import event, mouse
import os

#fix root dir
path = os.path.abspath(os.path.join('..', os.getcwd()))

pyglet.resource.path = [path] 
pyglet.resource.reindex()

#make window
window = pyglet.window.Window()

#object vars
#music = pyglet.resource.media('Assets/Images/music.mp3')
image = pyglet.image.load("Assets/Images/kitten.png")
label = pyglet.text.Label('Hewwo, worwd',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')

#draw on window update
@window.event
def on_key_press(symbol,modifiers):
    print('The '+str(symbol)+  ' Key was pressed, with mod '+str(modifiers))

@window.event
def on_mouse_press(x,y,button,modifiers):
    print(str(button)+'click')

@window.event
def on_draw():
    window.clear()
    image.blit(0,0)

pyglet.app.run()