import os
from ursina import Shader

# Get the root path of the directory
path = os.path.abspath(os.path.join('..', os.getcwd()))

def scriptImport(relPath):
    # import a script as a string
    file = open(os.path.join(path,relPath))
    code = str(file.read())
    file.close()
    return code


def shaderImport(**kwArgs):
    # A function to import a given glsl script as a ursina shader
    # syntax = <f, v, or g> = str(relPath)
    vert = str()
    frag = str()
    geom = str()
    for key,value in kwArgs.items():
        if key == 'f':
            frag = scriptImport(value)
        elif key == 'g':
            frag = scriptImport(value)
        elif key == 'v':
            vert = scriptImport(value)
    return Shader(
        fragment = frag,
        geometry= geom,
        vertex=vert
    )