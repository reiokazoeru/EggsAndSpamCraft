from ursina import *
import sys
import os

from ursina import entity

root = os.path.abspath(os.path.join('..', os.getcwd()))
assets = os.path.join(root,'Assets\\')
renderingScripts = os.path.join(assets,'Rendering Scripts\\')

sys.path.insert(0,str(renderingScripts))
from shaderMaker import shaderImport


def update():
    e.rotation_y += time.dt * 100
    e.rotation_x += time.dt * 100
    e.rotation_z += time.dt * 100

app = Ursina() # start runtime

window.title = 'My Gex'
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = True

e=Entity()
e.model = 'cube'
e.color = color.random_color()
e.position = (0,0,0)
e.scale = (5,5,5)

EditorCamera()
shad = shaderImport(f='Assets\\Rendering Scripts\\tests\\ursina rtx maybe\\glslPH.glsl')
camera.shader = shad



app.run()
