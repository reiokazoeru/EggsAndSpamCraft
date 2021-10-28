import pyglet
import os

#fix root dir
pyglet.resource.path = [os.path.abspath(os.path.join('..', os.getcwd()))] 
pyglet.resource.reindex()

#make window
window = pyglet.window.Window()

#object vars
image = pyglet.resource.image('Images/kitten.png')
label = pyglet.text.Label('Hewwo, worwd',
                          font_name='Times New Roman',
                          font_size=36,
                          x=window.width//2, y=window.height//2,
                          anchor_x='center', anchor_y='center')
#draw on window update
@window.event
def on_draw():
    window.clear()
    

pyglet.app.run()