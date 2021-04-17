import sys, pygame
from pygame.locals import *
from pygame.constants import *
# from pyglet.gl import *
from OpenGL.GL import *
from OpenGL.GLU import *
from tkinter import *
from tkinter import messagebox
from objbuilder import *
# IMPORT OBJECT LOADER
from objloader import *

def UpdateCoor(vertices, tx=0, ty=0, tz=0):
    for vertex in vertices:
        vertex[0] += tx
        vertex[1] += ty
        vertex[2] += tz

def Transform(tx=0, ty=0, tz=0, rx=0, ry=0, rz=0, sx=1, sy=1, sz=1):

    glMatrixMode(GL_PROJECTION)
    glTranslatef(tx, ty, tz)
    glRotatef(ry, 0, 1, 0)
    glRotatef(rx, 1, 0, 0)
    glRotatef(rz, 0, 0, 1)
    glScalef(sx, sy, sz)
    glMatrixMode(GL_MODELVIEW)

# glBindTexture(texture.target, texture.id)

def main():
    pygame.init()
    display = (1100, 650)
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
                    UpdateCoor(room_vertices, tx=-4)
                    UpdateCoor(floor_vertices, tx=-4)
                    UpdateCoor(ceil_vertices, tx=-4)
                    Transform(tx=4)
                    # monkey_position[0] += 4
                elif event.key == pygame.K_LEFT and count_x < 3:
                    count_x += 1
                    UpdateCoor(room_vertices, tx=4)
                    UpdateCoor(floor_vertices, tx=4)
                    UpdateCoor(ceil_vertices, tx=4)
                    Transform(tx=-4)
                    # monkey_position[0] -= 4
                elif event.key == pygame.K_UP and count_z < 2:
                    count_z += 1
                    UpdateCoor(room_vertices, tz=4)
                    UpdateCoor(floor_vertices, tz=4)
                    UpdateCoor(ceil_vertices, tz=4)
                    Transform(tz=-4)
                    # monkey_position[2] -= 4
                elif event.key == pygame.K_DOWN and count_z > -2:
                    count_z -= 1
                    UpdateCoor(room_vertices, tz=-4)
                    UpdateCoor(floor_vertices, tz=-4)
                    UpdateCoor(ceil_vertices, tz=-4)
                    Transform(tz=4)
                    # monkey_position[2] += 4
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

