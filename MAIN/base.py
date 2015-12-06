# This is the base module imported by all other Python Doom
# modules. Without this Python Doom don't work, so make sure
# you have this in your fork!
# ==========================================================
# Python Doom - Base Module
#
# . . . . . . . . . . . . . . . . . . . . . . . . . . . . Gustavo

from PIL import Image as i

class Vertex:
    xpos = 0
    ypos = 0
    zpos = 0
    linkedvertexes = []
    parentshape = None
    def changeVertexPosition(x, y, z):
        xpos = x
        ypos = y
        zpos = z
        
    if parentshape != None:
        relxpos = xpos - parentshape.xpos
        relypos = ypos - parentshape.ypos
        relzpos = zpos - parentshape.zpos

class Face:
    vertexes = []
    texture = i.image

class Shape:
    vertexes = []
    faces = []
    material = None
    pivotx = 0
    pivoty = 0
    pivotz = 0

    def changePivot(x, y, z):
        pivotx = x
        pivoty = y
        pivotz = z

def initialize:
    *.PreInitialization()
    *.Initialization()
    *.PostInitialization()

initialize()
