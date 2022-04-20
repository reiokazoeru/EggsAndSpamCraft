from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

root = os.path.abspath(os.path.join('..', os.getcwd()))
assets = os.path.join(root,'Assets\\')
renderingScripts = os.path.join(assets,'Rendering Scripts\\')

sys.path.insert(0,str(renderingScripts))
from shaderMaker import shaderImport


"""
x x x 
x x x
x x x
 - - -
| | | |
 - - -
| | | |
 - - -

"""


class Chunk:
    def genCubeVerts(c:tuple): # Generate all 8 points of a cube
        return [
            (c[0],c[1],c[2]),
            (c[0]+1,c[1],c[2]),
            (c[0]+1,c[1]+1,c[2]),
            (c[0],c[1]+1,c[2]),
            (c[0],c[1]+1,c[2]+1),
            (c[0]+1,c[1]+1,c[2]+1),
            (c[0]+1,c[1],c[2]+1),
            (c[0],c[1],c[2]+1)]
    def avgVerts(points:list):
        x = 0 
        y=0 
        z =0
        for i in points:
            x += i[0]
            y += i[1]
            z += i[2]
        x /= len(points)
        y /= len(points)
        z /= len(points)
        return [x,y,z]
    def findVertsandSquares(chunk_xyz):
        # convert chunk_xyz to squares with pos rel to chunk
        squares = [] # format: [(p1),(p2),(p3),(p4),type]
        for x in range(chunk_xyz):
            for y in range(chunk_xyz[x]):
                for z,block in (chunk_xyz[x][y]):
                    if block != 0:
                        if chunk_xyz[x][y][z+1] == 0:
                            squares.append([])
    def __init__(self,chunk_xyz,offset): #chunk in [x][y][z] format
        self.chunk_xyz = chunk_xyz
        self.offset = offset

def squareSignedDst(cP,pL): # cP is camera point, pL is the list of the points of the rectangle
    minX = 0
    maxX = 0
    minY = 0
    maxY = 0
    minZ = 0
    maxZ = 0
    for p in range(3):
        if pL[p][0]<minX:
            minx = pL[p][0]
        elif pL[p][0]>maxX:
            maxX = pL[p][0]
        if pL[p][1]<minY:
            minY = pL[p][0]
        elif pL[p][1]>maxY:
            maxY = pL[p][0]
        if pL[p][2]<minZ:
            minZ = pL[p][0]
        elif pL[p][2]>maxZ:
            maxZ = pL[p][0]





app = Ursina() # start ursina up

# window setup stuff
window.title = 'My Gex'
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.fps_counter.enabled = True




# instead of using mesh, use squares rendered
# works in this specific use case because we aint using weird quads, only squares

# define chunk size
chunk_size = (16,16,16)
# make empty chunk using [x][y][z]
chunk_space = [[[0 for i in range(chunk_size[2])] for i in range(chunk_size[1])] for i in range(chunk_size[0])]
# give the world a bottom
chunk_space[0][0] = [1 for i in range(chunk_size[2])]

# to get this to a usable point, i need a few things.
# while this format is easier to work with, it is a pain in the ass to render this way
# this will remedied by the chunk class






player = FirstPersonController()
app.run