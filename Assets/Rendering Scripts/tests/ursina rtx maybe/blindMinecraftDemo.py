from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

root = os.path.abspath(os.path.join('..', os.getcwd()))
assets = os.path.join(root,'Assets\\')
renderingScripts = os.path.join(assets,'Rendering Scripts\\')

sys.path.insert(0,str(renderingScripts))
from shaderMaker import shaderImport

app = Ursina() # start ursina up

# window stuff
window.title = 'My Gex'
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = True

worldSize = (16,16,16)
vertSize = (worldSize[0]+1,worldSize[1]+1,worldSize[2]+1)

worldSpace = [[[0 for i in range(worldSize[2])] for i in range(worldSize[1])] for i in range(worldSize[0])] #makes a 3d matrix for block stroage

vertSpace = [[[0 for i in range(vertSize[2])] for i in range(vertSize[1])] for i in range(vertSize[0])] #makes a 3d matrix for vertex stroage, updated by update loop


worldSpace[0][0] = [1 for i in range(worldSize[2])]

def genCubeVerts(c:tuple): # Generate all 8 potential points of a cube
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
def genWorldVerts(wSp): #make a grid of all points in mesh
    mainVert = [[[0 for i in range(vertSize[2])] for i in range(vertSize[1])] for i in range(vertSize[0])]
    # iterate for every 3d block
    for x in range(wSp):
        for y in range(wSp[x]):
            for z,block in enumerate(wSp[x][y]):
                if block != 0: # check for a block at the given position
                    tempVert = genCubeVerts((x,y,z)) # find all 8 potential verts of the block
                    # remove vertices that border another block
                    if wSp[x+1][y][z] != 0:
                        for p in [(x+1,y,z),(x+1,y+1,z),(x+1,y,z+1),(x+1,y+1,z+1)]:
                            tempVert.remove(p)
                    if wSp[x][y+1][z] != 0:
                        for p in [(x,y+1,z),(x+1,y+1,z),(x,y+1,z+1),(x+1,y+1,z+1)]:
                            if p in tempVert:
                                tempVert.remove(p)
                    if wSp[x][y][z+1] != 0:
                        for p in [(x+1,y,z+1),(x+1,y+1,z+1),(x,y+1,z+1),(x+1,y+1,z+1)]:
                            if p in tempVert:
                                tempVert.remove(p)
                    # place good verts on grid of all potential points
                    for p in tempVert:
                        mainVert[p[0]][p[1]][p[2]] = 1
    return mainVert # return the vert grid

def genWorldVertsAndTris(wSp,vSp): # make a usable tuples of verts and tris from block grid and from vert grid
    vertOut = [] # output var for verts
    triOut = [] # output var for tris
    # iterate for every 3d point
    for x in range(vSp):
        for y in range(vSp[x]):
            for z,vert in enumerate(vSp[x][y]):
                # check if there is a point on the grid, if so put it on the list of verts
                if vert == 1:
                    vertOut.append((x,y,z)) 
    for x in range(wSp):
        for y in range(wSp[x]):
            for z,block in enumerate(wSp[x][y]):
                # check every spot for a block
                if block != 0:
                    # check if tris are needed on that face by checking for a border block
                    # find verts on that face
                    # get index of the face points in the main vertex list
                    # add tri from points to tri list
                    if wSp[x+1][y][z] == 0:
                        xBP = [(x+1,y,z),(x+1,y+1,z),(x+1,y,z+1),(x+1,y+1,z+1)]
                        xBPi = [vertOut.index(i) for i in xBP]
                        triOut.append((xBPi[1],xBPi[2],xBPi[0]))
                        triOut.append((xBPi[2],xBPi[3],xBPi[0]))
                    if wSp[x-1][y][z] == 0:
                        nxBP = [(x,y,z),(x,y+1,z),(x,y+1,z+1),(x,y,z+1)]
                        nxBPi = [vertOut.index(i) for i in nxBP]
                        triOut.append((nxBPi[1],nxBPi[2],nxBPi[0]))
                        triOut.append((nxBPi[2],nxBPi[3],nxBPi[0]))
                    if wSp[x][y+1][z] == 0:
                        yBP = [(x,y+1,z),(x+1,y+1,z),(x,y+1,z+1),(x+1,y+1,z+1)]
                        yBPi = [vertOut.index(i) for i in yBP]
                        triOut.append((yBPi[1],yBPi[2],yBPi[0]))
                        triOut.append((yBPi[2],yBPi[3],yBPi[0]))
                    if wSp[x][y-1][z] == 0:
                        nyBP = [(x,y,z),(x+1,y,z),(x+1,y,z+1),(x,y,z+1)]
                        nyBPi = [vertOut.index(i) for i in nyBP]
                        triOut.append((nyBPi[1],nyBPi[2],nyBPi[0]))
                        triOut.append((nyBPi[2],nyBPi[3],nyBPi[0]))
                    if wSp[x][y][z+1] == 0:
                        zBP = [(x+1,y,z+1),(x+1,y+1,z+1),(x,y+1,z+1),(x+1,y+1,z+1)]
                        zBPi = [vertOut.index(i) for i in zBP]
                        triOut.append((zBPi[1],zBPi[2],zBPi[0]))
                        triOut.append((zBPi[2],zBPi[3],zBPi[0]))
                    if wSp[x][y][z-1] == 0:
                        nzBP = [(x,y,z),(x+1,y,z),(x+1,y+1,z),(x,y+1,z)]
                        nzBPi = [vertOut.index(i) for i in nzBP]
                        triOut.append((nzBPi[1],nzBPi[2],nzBPi[0]))
                        triOut.append((nzBPi[2],nzBPi[3],nzBPi[0]))
    return tuple(vertOut), tuple(triOut) # return the list of verts and tris as tuples as per the mesh function





player = FirstPersonController()
app.run