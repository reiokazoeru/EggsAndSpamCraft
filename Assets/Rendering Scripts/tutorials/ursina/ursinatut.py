from ursina import *

def update():
    cube.rotation_y += time.dt * 100
    if held_keys['t']:
        print(held_keys['t']) 


app = Ursina() # start runtime

window.title = 'My Gex'
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = True

cube = Entity(model='cube',color=color.orange,scale=(2,2,2))

app.run()