import pygame
import sys
from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    # x  y  z
    (-0.9, -0.9, 1),
    (-0.6, -1, 1),
    (-0.6, -0.8, 1),
    (-0.3, -0.8, 1),
    (-0.3, -1, 1),
    (0.3, -1, 1),
    (0.3, -0.8, 1),
    (0.6, -0.8, 1),
    (0.6, -1, 1),
    (1, -1, 1),
    (1, 1, 1),
    (0.1, 1, 1),
    (-0.3, 0, 1),
    (-1, -0.5, 1),

    (-0.9, -0.9, -1),
    (-0.6, -1, -1),
    (-0.6, -0.8, -1),
    (-0.3, -0.8, -1),
    (-0.3, -1, -1),
    (0.3, -1, -1),
    (0.3, -0.8, -1),
    (0.6, -0.8, -1),
    (0.6, -1, -1),
    (1, -1, -1),
    (1, 1, -1),
    (0.1, 1, -1),
    (-0.3, 0, -1),
    (-1, -0.5, -1),

    (-0.6, -0.5, 1),
    (-0.3, -0.5, 1),
    (0.3, -0.5, 1),
    (0.6, -0.5, 1),
    (1, -0.5, 1),
    (1, 0, 1),

    (-0.6, -0.5, -1),
    (-0.3, -0.5, -1),
    (0.3, -0.5, -1),
    (0.6, -0.5, -1),
    (1, -0.5, -1),
    (1, 0, -1),
)

# edges = (
#     (0, 1),
#     (0, 3),
#     (0, 4),
#     (2, 1),
#     (2, 3),
#     (2, 7),
#     (6, 3),
#     (6, 4),
#     (6, 7),
#     (5, 1),
#     (5, 4),
#     (5, 7)
# )

samping = (
    (13,0,1,28),
    (28,2,3,29),
    (29,4,5,30),
    (30,6,7,31),
    (31,8,9,32),
    (13,32,33,12),
    (12,33,10,11),
)

samping2 = (
    (27,14,15,34),
    (34,16,17,35),
    (35,18,19,36),
    (36,20,21,37),
    (37,22,23,38),
    (27,38,39,26),
    (26,39,24,25),
)


colors = (
    (1,1,1),
    (0,0,0),
    (0.7,0.5,1)
    )

surfaces = (
    (13,0,14,27),
    (12,13,27,26),
    (11,12,26,25),
    (10,11,25,24),
    (9,10,24,23),
)


def loadTexture():
    textureSurface = pygame.image.load('a25.jpg')
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
    width = textureSurface.get_width()
    height = textureSurface.get_height()

    glEnable(GL_TEXTURE_2D)
    texid = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texid)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, width, height,
                 0, GL_RGBA, GL_UNSIGNED_BYTE, textureData)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)

    return texid


def draw_cube():
    glBegin(GL_QUADS)
    
    x = 0

    glColor3fv(colors[2]);
    for surface in surfaces:
        for vertex in surface:
            glVertex3fv(verticies[vertex])

    glColor3fv(colors[0])
    for surface in samping:
        x+=1
        for vertex in surface:
            glVertex3fv(verticies[vertex])

    glColor3fv(colors[0])
    for surface in samping2:
        x+=1
        for vertex in surface:
            glVertex3fv(verticies[vertex])

    glEnd()

pygame.init()
display = (800, 600)
screen = pygame.display.set_mode(
    display, pygame.DOUBLEBUF | pygame.OPENGL | pygame.OPENGLBLIT)

loadTexture()

gluPerspective(45, display[0] / display[1], 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

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

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    draw_cube()

    pygame.display.flip()