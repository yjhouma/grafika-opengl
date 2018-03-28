import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from math import *

#berupa edge, hubungan-hubungan antara dua titik_sudut
#menunjukan titik sudut mana saja yang berhubungan

warna = (
    (0, 0, 1),
    (0, 1, 0),
    (1, 0, 0)
)

def Gedung():
    sisi_gedung = (
        (-2.1, 0),
        (-2.1, 1),
        (-2, 1),
        (-2, 0.3),
        (-1.70, 0.3),
        (-1.70, 0),
    )

    list_gedung = (
        (
            (-21, 0),
            (-21, 10),
            (-20, 10),
            (-20, 6),
            (-17, 6),
            (-17, 0),
        ), (
            (-17, 0),
            (-17, 3),
            (1, 3),
            (1, 0)
        ), (
            (1, 0),
            (1, 14),
            (3, 14),
            (3, 0)
        ), (
            (3, 0),
            (3, 7),
            (21, 7),
            (21, 0)
        )
    )

    for list in list_gedung :
        glBegin(GL_POLYGON)
        glColor3fv((0,0,0.3));
        for sisi in list :
            glVertex2fv((sisi[0],sisi[1]))
        glEnd()
    for list in list_gedung :
        glBegin(GL_POLYGON)
        glColor3fv((0,0,0.3));
        for sisi in list :
            glVertex2fv((sisi[0]+21,sisi[1]))
        glEnd()
    for list in list_gedung :
        glBegin(GL_POLYGON)
        glColor3fv((0,0,0.3));
        for sisi in list :
            glVertex2fv((sisi[0]+42,sisi[1]))
        glEnd()

def Langit():
    glBegin(GL_POLYGON)
    glColor3fv((1,0.627,0.004));
    glVertex2fv((-30,0));
    glVertex2fv((-30,30));
    glVertex2fv((30,30));
    glVertex2fv((30,0));
    glEnd()

def GarisJalan():
    glBegin(GL_POLYGON)
    glColor3fv((1,1,1))
    glVertex2fv((-30,-10.5))
    glVertex2fv((-30,-9.5))
    glVertex2fv((30,-9.5))
    glVertex2fv((30,-10.5))
    glEnd()

def mobil():
    titik_sudut = (
        (-2, 3),
        (2, 3),
        (3, 0),
        (6, 0),
        (6, -3),
        (-6, -3),
        (-6, 0),
        (-3, 0),
    )

    sisi_sisi = (
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 5),
        (5, 6),
        (6, 7),
        (7, 0),
        (0, 1),
    )

    permukaan = (
        (1, 2, 3, 4, 5, 6, 7,1),
    )

    glBegin(GL_POLYGON)
    glColor3fv((1, 0, 0))
    for sisi in sisi_sisi:
        for sudut in sisi:
            glVertex2fv(titik_sudut[sudut])
    glEnd()


def ban(x, y):
    radius = 2
    posx = x
    posy = y
    sides = 360
    edges = []

    glBegin(GL_POLYGON)
    glColor3fv((1,.7,0.5 ))
    for i in range(sides):
        posx_cosine = radius * cos(i*2*pi/sides) + posx
        posy_sines = radius * sin(i*2*pi/sides) +posy
        glVertex2fv((posx_cosine, posy_sines))
    glEnd()

    glBegin(GL_LINES)
    titik_titik = [(posx, posy), (posx+radius, posy)]
    edges = [(0, 1)]
    for i in range(1, sides):
        if i % 60 == 0:
            posx_cosine = radius * cos(i * 2 * pi / sides) + posx
            posy_sines = radius * sin(i * 2 * pi / sides) + posy
            titik_titik.append((posx_cosine, posy_sines))
            edges.append((0, i//60 + 1))

    for sisi in edges:
        for sudut in sisi:
            glVertex2fv(titik_titik[sudut])
            glColor3fv((1, 1, 1))
    glEnd()

#program utama
def main():
    pygame.init()
    ukuran_layar = (800,600)

    pygame.display.set_mode(ukuran_layar, DOUBLEBUF|OPENGL)
    gluPerspective(45, (ukuran_layar[0]/ukuran_layar[1]), 0.1, 0.0)
    glTranslatef(0, 0.0, -50)

    x = [-0.01]
    sudut = [0]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #clear frame
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)


        #pemandangan
        Langit()
        glPushMatrix()
        glTranslatef(x[0], 0, 0)
        Gedung()
        glPopMatrix()
        GarisJalan()
        x[0] -=0.1

        #mobil dan ban
        mobil()

        glPushMatrix()
        glTranslatef(-4, -4.5, 0);
        glRotatef(sudut[0], 0.0, 0.0, 1.0)
        ban(0, 0)
        glTranslatef(4, 4.5, 0)
        glPopMatrix()

        glPushMatrix()
        glTranslatef(4, -4.5, 0);
        glRotatef(sudut[0], 0.0, 0.0, 1.0)
        ban(0, 0)
        glTranslatef(-4, 4.5, 0)
        glPopMatrix()

        sudut[0] -= 15

        pygame.display.flip()

        pygame.time.wait(10)


main()
