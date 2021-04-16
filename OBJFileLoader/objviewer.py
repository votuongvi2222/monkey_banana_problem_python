import sys, pygame
from pygame.locals import *
from pygame.constants import *
# from pyglet.gl import *
from OpenGL.GL import *
from OpenGL.GLU import *
from tkinter import *
from tkinter import messagebox

# IMPORT OBJECT LOADER
from objloader import *

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

def Transform(tx=0, ty=0, tz=0, rx=0, ry=0, rz=0, sx=1, sy=1, sz=1):

    glMatrixMode(GL_PROJECTION)
    glTranslatef(tx, ty, tz)
    glRotatef(ry, 0, 1, 0)
    glRotatef(rx, 1, 0, 0)
    glRotatef(rz, 0, 0, 1)
    glScalef(sx, sy, sz)
    glMatrixMode(GL_MODELVIEW)

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

def Chair():
    glBegin(GL_QUADS)
    for surface in CUBE_SURFACES:
        x = 0
        for vertex_index in surface:
            x+=1
            glColor3fv(CHAIR_COLORS[x])
            glVertex3fv(chair_vertices[vertex_index])
    glEnd()
    glBegin(GL_LINES)
    for edge in chair_edges:
        for vertex_index in edge:
            # glColor3fv((1,1,1))
            glVertex3fv(chair_vertices[vertex_index])
    glEnd()
# glBindTexture(texture.target, texture.id)

def main():
    pygame.init()
    display = (1180, 650)
    screen = pygame.display.set_mode(display, DOUBLEBUF|OPENGLBLIT)

    glMatrixMode(GL_PROJECTION)
    # glLoadIdentity()
    ratio = 50
    gluPerspective(ratio, (display[0]/display[1]), 0.5, 50.0)
    glTranslatef(0, -10, -34)
    glMatrixMode(GL_MODELVIEW)

    glEnable(GL_COLOR_MATERIAL)
    glShadeModel(GL_SMOOTH)           # most obj files expect to be smooth-shaded

    # LOAD OBJECT AFTER PYGAME INIT
    chair_obj = OBJ('obj_files/chair.obj')
    chair_obj.generate()
    monkey_obj = OBJ('obj_files/monkey.obj')
    monkey_obj.generate()
    banana_obj = OBJ('obj_files/banana.obj')
    banana_obj.generate()

    monkey_step_lenght = 1
    count_z, count_x, count_y = (0, 0, 0)
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and count_x > -3:
                    count_x -= 1
                    Transform(tx=0.2, ry=360-5)
                    monkey_position[0] += 4
                elif event.key == pygame.K_LEFT and count_x < 3:
                    count_x += 1
                    Transform(tx=-0.2, ry=5)
                    monkey_position[0] -= 4
                elif event.key == pygame.K_UP and count_z < 2:
                    count_z += 1
                    monkey_position[2] -= 4
                elif event.key == pygame.K_DOWN and count_z > -2:
                    count_z -= 1
                    monkey_position[2] += 4
                elif event.key == pygame.K_RETURN:
                    if count_y == 0:
                        count_y = 1
                        monkey_position[1] += 1.2
                    elif count_y == 1:
                        count_y = 0
                        monkey_position[1] -= 1.2
    
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # RENDER OBJECT
        Room()
        Monkey()
        # glLoadIdentity()

        
        glEnable(GL_DEPTH_TEST)
        chair_obj.render()
        monkey_obj.render()
        banana_obj.render()
        glDisable(GL_DEPTH_TEST)
        

        pygame.display.flip()

if __name__ == "__main__":
    main()

