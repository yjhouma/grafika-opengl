import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


verticies = (
    (-1, -1, 1,1),
    (-0.6, -1, 1,1),
    (-0.6, -0.8, 1,1),
    (-0.3, -0.8, 1,1),
    (-0.3, -1, 1,1),
    (0.3, -1, 1,1),
    (0.3, -0.8, 1,1),
    (0.6, -0.8, 1,1),
    (0.6, -1, 1,1),
    (1, -1, 1,1),
    (1, 1, 1,1),
    (0.1, 1, 1,1),
    (-0.3, 0, 1,1),
    (-1, -0.5, 1,1),

    (-1, -1, -1,1),
    (-0.6, -1, -1,1),
    (-0.6, -0.8, -1,1),
    (-0.3, -0.8, -1,1),
    (-0.3, -1, -1,1),
    (0.3, -1, -1,1),
    (0.3, -0.8, -1,1),
    (0.6, -0.8, -1,1),
    (0.6, -1, -1,1),
    (1, -1, -1,1),
    (1, 1, -1,1),
    (0.1, 1, -1,1),
    (-0.3, 0, -1,1),
    (-1, -0.5, -1,1),

    (-0.6, -0.5, 1,1),
    (-0.3, -0.5, 1,1),
    (0.3, -0.5, 1,1),
    (0.6, -0.5, 1,1),
    (1, -0.5, 1,1),
    (1, 0, 1,1),

    (-0.6, -0.5, -1,1),
    (-0.3, -0.5, -1,1),
    (0.3, -0.5, -1,1),
    (0.6, -0.5, -1,1),
    (1, -0.5, -1,1),
    (1, 0, -1,1),
    )

colors = (
    (1,1,1),
    (0,1,1),
    (1,0,1)
    )

surfaces = (
    (13,0,14,27),
    (12,13,27,26),
    (11,12,26,25),
    (10,11,25,24),
    (9,10,24,23),
    )

def Car():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glShadeModel(GL_SMOOTH)
    glBegin(GL_QUADS)
    
    x = 0

    glColor3fv(colors[2]);
    for surface in surfaces:
        for vertex in surface:
            glVertex4fv(verticies[vertex])

    glEnd()


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(0.0,0.0, -5)

    glRotatef(0,0,0,0)
    glEnable(GL_DEPTH_TEST)
    glDepthMask(GL_TRUE)
    glDepthFunc(GL_LEQUAL)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glRotatef(2, 0, -1, 0)
                if event.key == pygame.K_RIGHT:
                    glRotatef(2, 0 , 1, 0)
                if event.key == pygame.K_UP:
                    glRotatef(2, 1, 0, 0)
                if event.key == pygame.K_DOWN:
                    glRotatef(2, -1, 0, 0)
        #glRotatef(1,1,3,1)
        #glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        #pygame.time.wait(10)
        
        glDepthRange(0.0, 1.0)

        Car()
        pygame.display.flip()

        pygame.time.wait(10)


main()
