import sys, pygame
from pygame.locals import *
from pygame.constants import *
# from pyglet.gl import *
from OpenGL.GL import *
from OpenGL.GLU import *

monkey_position = [0, 0, 0]
room_vertices = [
    [16, 0, -12],
    [16, 20, -12],
    [-16, 20, -12],
    [-16, 0, -12],
    [16, 0, 12],
    [16, 20, 12],
    [-16, 20, 12],
    [-16, 0, 12]
]
room_edges = [
    [0,1],
    [0,3],
    [0,4],
    [2,1],
    [2,3],
    [2,6],
    [7,3],
    [7,4],
    [7,6],
    [5,1],
    [5,4],
    [5,6]
    ]

floor_vertices = [
    [16, 0, -12],
    [-16, 0, -12],
    [-16, 0, 12],
    [16, 0, 12],
    [12, 0, -12],
    [12, 0, 12],
    [8, 0, -12],
    [8, 0, 12],
    [4, 0, -12],
    [4, 0, 12],
    [0, 0, -12],
    [0, 0, 12],
    [-12, 0, -12],
    [-12, 0, 12],
    [-8, 0, -12],
    [-8, 0, 12],
    [-4, 0, -12],
    [-4, 0, 12],
    [16, 0, 8],
    [-16, 0, 8],
    [16, 0, 4],
    [-16, 0, 4],
    [16, 0, 0],
    [-16, 0, 0],
    [16, 0, -8],
    [-16, 0, -8],
    [16, 0, -4],
    [-16, 0, -4]
    ]

floor_edges = [
    [0, 1],
    [0, 3],
    [1, 2],
    [2, 3],
    [4, 5],
    [6, 7],
    [8, 9],
    [10, 11],
    [12, 13],
    [14, 15],
    [16, 17],
    [18, 19],
    [20, 21],
    [22, 23],
    [24, 25],
    [26, 27]
    ]

ceil_vertices = [
    [16, 20, -12],
    [-16, 20, -12],
    [-16, 20, 12],
    [16, 20, 12],
    [12, 20, -12],
    [12, 20, 12],
    [8, 20, -12],
    [8, 20, 12],
    [4, 20, -12],
    [4, 20, 12],
    [0, 20, -12],
    [0, 20, 12],
    [-12, 20, -12],
    [-12, 20, 12],
    [-8, 20, -12],
    [-8, 20, 12],
    [-4, 20, -12],
    [-4, 20, 12],
    [16, 20, 8],
    [-16, 20, 8],
    [16, 20, 4],
    [-16, 20, 4],
    [16, 20, 0],
    [-16, 20, 0],
    [16, 20, -8],
    [-16, 20, -8],
    [16, 20, -4],
    [-16, 20, -4]
    ]

ceil_edges = [
    [0, 1],
    [0, 3],
    [1, 2],
    [2, 3],
    [4, 5],
    [6, 7],
    [8, 9],
    [10, 11],
    [12, 13],
    [14, 15],
    [16, 17],
    [18, 19],
    [20, 21],
    [22, 23],
    [24, 25],
    [26, 27]
    ]

chair_vertices = [
    [0.5, -5, -0.5],
    [0.5, -4, -0.5],
    [-0.5, -4, -0.5],
    [-0.5, -5, -0.5],
    [0.5, -5, 0.5],
    [0.5, -4, 0.5],
    [-0.5, -4, 0.5],
    [-0.5, -5, 0.5]
]

chair_edges = [
    [0,1],
    [0,3],
    [0,4],
    [2,1],
    [2,3],
    [2,6],
    [7,3],
    [7,4],
    [7,6],
    [5,1],
    [5,4],
    [5,6]
    ]
ROOM_COLORS = [
    [0,1,195/255],
    [0,130/255,106/255],
    [0,120/255,100/255],
    [0,110/255,95/255],
    [0,100/255,85/255],
    [1,1,1],
    [0,1,195/255],
    [0,130/255,106/255],
    [0,120/255,100/255],
    [0,110/255,95/255],
    [0,100/255,85/255],
    [1,1,1]
    ]

CHAIR_COLORS = [
    [209/255,118/255,0],
    [200/255,110/255,0],
    [190/255,100/255,0],
    [185/255,95/255,0],
    [180/255,90/255,0],
    [1,1,1],
    [209/255,118/255,0],
    [200/255,110/255,0],
    [190/255,100/255,0],
    [185/255,95/255,0],
    [180/255,90/255,0],
    [1,1,1]
    ]
CUBE_SURFACES = [
    [0,1,2,3],
    [3,2,6,7],
    [7,6,5,4],
    [4,5,1,0],
    [1,5,6,2],
    [4,0,3,7]
    ]

def Monkey():
    glEnable(GL_POINT_SMOOTH)
    glPointSize(5)

    glBegin(GL_POINTS)
    glColor3d(1, 1, 1)
    glVertex3d(monkey_position[0], monkey_position[1], monkey_position[2])
    glEnd()

def Room():
    # draw the surfaces of the room
    glBegin(GL_QUADS)
    for surface in CUBE_SURFACES:
        x = 0
        for vertex_index in surface:
            x+=1
            glColor3fv(ROOM_COLORS[x])
            glVertex3fv(room_vertices[vertex_index])
    glEnd()
    # draw the edges of the room
    glBegin(GL_LINES)
    for edge in room_edges:
        for vertex_index in edge:
            glVertex3fv(room_vertices[vertex_index])
    glEnd()
    # draw the ceil
    glBegin(GL_LINES)
    for edge in ceil_edges:
        for vertex_index in edge:
            glVertex3fv(ceil_vertices[vertex_index])
    glEnd()
    # draw the floor
    glBegin(GL_LINES)
    for edge in floor_edges:
        for vertex_index in edge:
            glColor3fv((42/255, 147/255, 121/255))
            glVertex3fv(floor_vertices[vertex_index])
    glEnd()
