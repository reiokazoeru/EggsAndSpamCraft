from ursina import *

def update(): #updates per frame
    cube.rotation_y += time.dt * 100
    if held_keys['t']:
        cube.rotation_y += time.dt * 100

def dictToEnts(d:dict):
    pass



app = Ursina() # start runtime

# window setup
window.title = 'My Gex'
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = True

#gex
shader = Shader(language=Shader.GLSL,
    vertex='''
#version 430

in vec4 p3d_Vertex;
uniform mat4 p3d_ViewMatrixInverse;
in vec2 p3d_MultiTexCoord0;
out vec2 uv;

void main() {
    gl_Position = p3d_ViewMatrixInverse  * p3d_Vertex;
    uv = p3d_MultiTexCoord0;
}
''',

fragment='''
#version 430

uniform sampler2D tex;
in vec2 uv;
out vec4 color;

void main() {
    vec3 rgb = texture(tex, uv).rgb;
    color = vec4(rgb, 1.0);
}

''')
cube = Entity(model='cube',color=color.orange,scale=(2,2,2))
camera.shader = shader


app.run()