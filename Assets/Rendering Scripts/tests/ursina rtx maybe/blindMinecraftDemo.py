from random import triangular
from ursina import *

root = os.path.abspath(os.path.join('..', os.getcwd()))
assets = os.path.join(root,'Assets\\')
renderingScripts = os.path.join(assets,'Rendering Scripts\\')

sys.path.insert(0,str(renderingScripts))
from shaderMaker import shaderImport

worldSize = (16,16,16)
vertSize = (worldSize[0]+1,worldSize[1]+1,worldSize[2]+1)

worldSpace = [[[0 for i in range(worldSize[2])] for i in range(worldSize[1])] for i in range(worldSize[0])] #makes a 3d matrix for block stroage

vertSpace = [[[0 for i in range(vertSize[2])] for i in range(vertSize[1])] for i in range(vertSize[0])] #makes a 3d matrix for vertex stroage, updated by update loop
triSpace = [[[0 for i in range(worldSize[2])] for i in range(worldSize[1])] for i in range(worldSize[0])]

worldSpace[0][0] = [1 for i in range(worldSize[2])]

def genCubeVerts(c):
    return [
        (c[0],c[1],c[2]),
        (c[0]+1,c[1],c[2]),
        (c[0]+1,c[1]+1,c[2]),
        (c[0],c[1]+1,c[2]),
        (c[0],c[1]+1,c[2]+1),
        (c[0]+1,c[1]+1,c[2]+1),
        (c[0]+1,c[1],c[2]+1),
        (c[0],c[1],c[2]+1)
    ]
def genWorldVerts(wSp):
    mainVert = [[[0 for i in range(vertSize[2])] for i in range(vertSize[1])] for i in range(vertSize[0])]
    # iterate for every 3d point
    for x in range(wSp):
        for y in range(wSp[x]):
            for z,block in enumerate(wSp[x][y]):
                xBorderPoints = [(x+1,y,z),(x+1,y+1,z),(x+1,y,z+1),(x+1,y+1,z+1)]
                yBorderPoints = [(x,y+1,z),(x+1,y+1,z),(x,y+1,z+1),(x+1,y+1,z+1)]
                zBorderPoints = [(x+1,y,z+1),(x+1,y+1,z+1),(x,y+1,z+1),(x+1,y+1,z+1)]
                if block != 0:
                    tempVert = genCubeVerts((x,y,z))
                    if wSp[x+1][y][z] != 0:
                        for p in xBorderPoints:
                            tempVert.remove(p)
                    if wSp[x][y+1][z] != 0:
                        for p in yBorderPoints:
                            if p in tempVert:
                                tempVert.remove(p)
                    if wSp[x][y][z+1] != 0:
                        for p in zBorderPoints:
                            if p in tempVert:
                                tempVert.remove(p)
                    for p in tempVert:
                        mainVert[p[0]][p[1]][p[2]] = 1
    return mainVert

def genWorldTris(wSp,vSp):
    mainLine = [[[0 for i in range(worldSize[2])] for i in range(worldSize[1])] for i in range(worldSize[0])]
    # iterate for every 3d point
    for x in range(wSp):
        for y in range(wSp[x]):
            for z,block in enumerate(wSp[x][y]):
                if block != 0:
                    curVerts = genCubeVerts((x,y,z))
                    if wSp[x+1][y][z] == 0:
                        pass
                    if wSp[x][y+1][z] == 0:
                        pass
                    if wSp[x][y][z+1] == 0:
                        pass
                    if wSp[x-1][y][z] == 0:
                        pass
                    if wSp[x][y-1][z] == 0:
                        pass
                    if wSp[x][y][z-1] == 0:
                        pass

def update():
    pass



app = Ursina() # start ursina up

# window stuff
window.title = 'My Gex'
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = True

app.run