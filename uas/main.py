# Basic OBJ file viewer. needs objloader from:
#  http://www.pygame.org/wiki/OBJFileLoader
# LMB + move: rotate
# RMB + move: pan
# Scroll wheel: zoom in/out
import sys, pygame, math
from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random

# IMPORT OBJECT LOADER

angle = 0.0

def Car():
    # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glShadeModel(GL_SMOOTH)
    glBegin(GL_QUADS)                
    
    glColor3f(1,1,0)
    glVertex3f( 0.2, 0.4,0.6)
    glVertex3f(0.6, 0.5,0.6)
    glVertex3f(0.6, 0.5,0.2)
    glVertex3f( 0.2,0.4,0.2)

    glVertex3f( 0.2,0.2,0.6)
    glVertex3f(0.6,0.2,0.6)
    glVertex3f(0.6,0.2,0.2)
    glVertex3f( 0.2,0.2,0.2)

    glVertex3f( 0.2,0.2,0.6)
    glVertex3f(0.2, 0.4,0.6)
    glVertex3f(0.2,0.4,0.2)
    glVertex3f( 0.2,0.2,0.2)

    glVertex3f(0.6,0.2,0.6)
    glVertex3f(0.6,0.5,0.6)
    glVertex3f(0.6,0.5,0.2)
    glVertex3f( 0.6,0.2,0.2)

    glVertex3f(0.2,0.2,0.6)
    glVertex3f(0.6,0.2,0.6)
    glVertex3f(0.6,0.5,0.6)
    glVertex3f(0.2,0.4,0.6)

    glVertex3f(0.2,0.2,0.2)
    glVertex3f( 0.6,0.2,0.2)
    glVertex3f( 0.6,0.5,0.2)
    glVertex3f( 0.2,0.4,0.2)
    glVertex3f(0.7,0.65,0.6)
    glVertex3f(0.7,0.65,0.2)
    glVertex3f(1.7,0.65,0.2)
    glVertex3f(1.7,0.65,0.6)

    glColor3f(0,1,0)
    glVertex3f( 1.8, 0.5,0.6)
    glVertex3f(1.8, 0.5,0.2)
    glVertex3f(2.1, 0.4, 0.2)
    glVertex3f(2.1,0.4,0.6)

    glVertex3f( 2.1,0.2,0.6)
    glVertex3f(2.1,0.2,0.2)
    glVertex3f(1.8,0.2,0.6)
    glVertex3f( 1.8,0.2,0.6)

    glVertex3f(2.1,0.4,0.6)
    glVertex3f(2.1,0.4,0.2)
    glVertex3f(2.1,0.2,0.2)
    glVertex3f(2.1,0.2,0.6)

    glVertex3f(1.8,0.2,0.2)
    glVertex3f(1.8,0.5,0.2)
    glVertex3f(2.1,0.4,0.2)
    glVertex3f(2.1,0.2,0.2)

    glVertex3f(1.8,0.2,0.6)
    glVertex3f(1.8,0.5,0.6)
    glVertex3f(2.1,0.4,0.6)
    glVertex3f(2.1,0.2,0.6)
    glVertex3f( 0.6, 0.5,0.6)
    glVertex3f(0.6, 0.2,0.6)
    glVertex3f(1.8, 0.2, 0.6)
    glVertex3f(1.8,0.5,0.6)

    glVertex3f( 0.6,0.2,0.6)
    glVertex3f(0.6,0.2,0.2)
    glVertex3f(1.8,0.2,0.2)
    glVertex3f( 1.8,0.2,0.6)

    glVertex3f(0.6,0.5,0.2)
    glVertex3f(0.6,0.2,0.2)
    glVertex3f(1.8,0.2,0.2)
    glVertex3f(1.8,0.5,0.2)

    glColor3f(0.3,0.3,0.3)
    glVertex3f( 0.77, 0.63,0.2)
    glVertex3f(0.75, 0.5,0.2)
    glVertex3f(1.2, 0.5, 0.2)
    glVertex3f( 1.22,0.63,0.2)

    glVertex3f(1.27,0.63,.2)
    glVertex3f(1.25,0.5,0.2)
    glVertex3f(1.65,0.5,0.2)
    glVertex3f(1.67,0.63,0.2)

    glColor3f(0,0,1)
    glVertex3f(0.7,0.65,0.2)
    glVertex3f(0.7,0.5,.2)  
    glVertex3f(0.75,0.5,0.2)
    glVertex3f(0.77,0.65,0.2)

    glVertex3f(1.2,0.65,0.2)
    glVertex3f(1.2,0.5,.2)   
    glVertex3f(1.25,0.5,0.2)
    glVertex3f(1.27,0.65,0.2)

    glVertex3f(1.65,0.65,0.2)
    glVertex3f(1.65,0.5,.2)
    glVertex3f(1.7,0.5,0.2)
    glVertex3f(1.7,0.65,0.2)

    glVertex3f( 0.75, 0.65,0.2)
    glVertex3f(0.75, 0.63,0.2) 
    glVertex3f(1.7, 0.63, 0.2)
    glVertex3f( 1.7,0.65,0.2)

    glVertex3f( 0.75, 0.65,0.6)
    glVertex3f(0.75, 0.63,0.6)  
    glVertex3f(1.7, 0.63, 0.6)
    glVertex3f( 1.7,0.65,0.6)

    glColor3f(0.3,0.3,0.3)
    glVertex3f( 0.77, 0.63,0.6)
    glVertex3f(0.75, 0.5,0.6) 
    glVertex3f(1.2, 0.5, 0.6)
    glVertex3f( 1.22,0.63,0.6)

    glVertex3f(1.27,0.63,.6)
    glVertex3f(1.25,0.5,0.6)      
    glVertex3f(1.65,0.5,0.6)
    glVertex3f(1.67,0.63,0.6)

    glColor3f(0,1,1)
    glVertex3f(0.7,0.65,0.6)
    glVertex3f(0.7,0.5,.6)        
    glVertex3f(0.75,0.5,0.6)
    glVertex3f(0.77,0.65,0.6)

    glVertex3f(1.2,0.65,0.6)
    glVertex3f(1.2,0.5,.6)         
    glVertex3f(1.25,0.5,0.6)
    glVertex3f(1.27,0.65,0.6)

    glVertex3f(1.65,0.65,0.6)
    glVertex3f(1.65,0.5,.6)
    glVertex3f(1.7,0.5,0.6)
    glVertex3f(1.7,0.65,0.6)
    
    glColor3f(0.3,0.3,0.3)
    glVertex3f( 0.6, 0.5,0.6)
    glVertex3f(0.6, 0.5,0.2)           
    glVertex3f(0.7, 0.65, 0.2)
    glVertex3f( 0.7,0.65,0.6)

    glVertex3f(1.7,0.65,.6)
    glVertex3f(1.7,0.65,0.2)           
    glVertex3f(1.8,0.5,0.2)
    glVertex3f(1.8,0.5,0.6)

    glEnd()

    glBegin(GL_TRIANGLES)

    glColor3f(0.3,0.3,0.3)
    glVertex3f( 0.6, 0.5,0.6)
    glVertex3f( 0.7,0.65,0.6)       
    glVertex3f(0.7,0.5,0.6)

    glVertex3f( 0.6, 0.5,0.2)
    glVertex3f( 0.7,0.65,0.2)      
    glVertex3f(0.7,0.5,0.2)

    glVertex3f( 1.7, 0.65,0.2)
    glVertex3f( 1.8,0.5,0.2)
    glVertex3f( 1.7,0.5,0.2)

    glVertex3f( 1.7, 0.65,0.6)
    glVertex3f( 1.8,0.5,0.6)    
    glVertex3f(1.7,0.5,0.6)

    glEnd()

    glPushMatrix()
    glColor3f(0.7,0.7,0.7)
    glTranslatef(1.65,0.2,0.3)
    glRotatef(90.0,0,1,0)
    
    t = gluNewQuadric()
    gluQuadricDrawStyle(t, GLU_FILL)

    gluCylinder(t,0.02,0.03,.5,10,10)
    glPopMatrix()

    glColor3f(0.7,0.7,0.7)
    glPushMatrix()
    glBegin(GL_LINE_STRIP);
    
    for theta in range(0, 360) :
        glVertex3f(0.6,0.2,0.62);
        glVertex3f(0.6+(0.08*(math.cos(((theta+angle)*3.14)/180))),0.2+(0.08*(math.sin(((theta+angle)*3.14)/180))),0.62);
        theta = theta + 20
    
    glEnd();

    glBegin(GL_LINE_STRIP);
    for theta in range(0, 360) :
        glVertex3f(0.6,0.2,0.18);
        glVertex3f(0.6+(0.08*(math.cos(((theta+angle)*3.14)/180))),0.2+(0.08*(math.sin(((theta+angle)*3.14)/180))),0.18);
        theta = theta + 20

    glEnd();

    glBegin(GL_LINE_STRIP);
    for theta in range(0, 360) :
        glVertex3f(1.7,0.2,0.18);
        glVertex3f(1.7+(0.08*(math.cos(((theta+angle)*3.14)/180))),0.2+(0.08*(math.sin(((theta+angle)*3.14)/180))),0.18);
        theta = theta + 20

    glEnd();

    glBegin(GL_LINE_STRIP);
    for theta in range(0, 360) :
        glVertex3f(1.7,0.2,0.62);
        glVertex3f(1.7+(0.08*(math.cos(((theta+angle)*3.14)/180))),0.2+(0.08*(math.sin(((theta+angle)*3.14)/180))),0.62);
        theta = theta + 20

    glEnd();

    glTranslatef(0.6,0.2,0.6);
    glColor3f(0,0,0);
    # glutSolidTorus(0.025,0.07,10,25);

    glTranslatef(0,0,-0.4);
    # glutSolidTorus(0.025,0.07,10,25);

    glTranslatef(1.1,0,0);
    # glutSolidTorus(0.025,0.07,10,25);

    glTranslatef(0,0,0.4);
    # glutSolidTorus(0.025,0.07,10,25);
    glPopMatrix();

    # glPopMatrix();
    # glEnable(GL_DEPTH_TEST);
    # glutPostRedisplay();
    # glutSwapBuffers();

def mainMobil():
    red = (255,255,255,255)
    pygame.init()
    viewport = (800,600)
    hx = viewport[0]/2
    hy = viewport[1]/2
    srf = pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)

    glLightfv(GL_LIGHT0, GL_POSITION,  (-40, 0, 0, 0.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (float(red[0]) / 256, float(red[1]) / 256, float(red[2]) / 256, 1.0))
    glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION,  (40, 0, 0, 0.0))
    glLightfv(GL_LIGHT0, GL_SPOT_CUTOFF,  10)

    glEnable(GL_LIGHT0)

    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)           # most obj files expect to be smooth-shaded

    # LOAD OBJECT AFTER PYGAME INIT
    # obj = OBJ(sys.argv[1], swapyz=True)

    clock = pygame.time.Clock()

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    width, height = viewport
    gluPerspective(90.0, width/float(height), 1, 100.0)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_MODELVIEW)


    rx, ry = (0,0)
    tx, ty = (0,0)
    zpos = 5
    rotate = move = False
    # itera = 0
    loopitera = 0
    iteraList = []
    iteraList.append(0) #dummy
    # bagian hujan
    hujanPoint = []
    hujanIte = -1
    rainspeed = float(red[3]) / 2550
    knalpotspeed = float(255) / 127.5
    while hujanIte < 1 :
        hujanPoint.append([hujanIte, random.uniform(-1,1)])
        hujanIte += 0.03
    while 1:
        clock.tick(30)
        for e in pygame.event.get():
            if e.type == QUIT:
                sys.exit()
            elif e.type == KEYDOWN and e.key == K_ESCAPE:
                sys.exit()
            elif e.type == MOUSEBUTTONDOWN:
                if e.button == 4: zpos = max(1, zpos-1)
                elif e.button == 5: zpos += 1
                elif e.button == 1: rotate = True
                elif e.button == 3: move = True
            elif e.type == MOUSEBUTTONUP:
                if e.button == 1: rotate = False
                elif e.button == 3: move = False
            elif e.type == MOUSEMOTION:
                i, j = e.rel
                if rotate:
                    rx += i
                    ry += j
                if move:
                    tx += i
                    ty -= j

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        for hujan in range(len(hujanPoint)):
            glBegin(GL_QUADS)
            glColor3f(255,255,255)
            glVertex3f(hujanPoint[hujan][0] + 0.005  ,hujanPoint[hujan][1] + 0.05,-1)
            glVertex3f(hujanPoint[hujan][0] + 0.005  ,hujanPoint[hujan][1],-1)
            glVertex3f(hujanPoint[hujan][0]         ,hujanPoint[hujan][1],  -1)
            glVertex3f(hujanPoint[hujan][0]         ,hujanPoint[hujan][1] + 0.05,-1)
            glEnd()
            hujanPoint[hujan][1] -= rainspeed
            if hujanPoint[hujan][1] < -1:
                hujanPoint[hujan][1] = 1
        # RENDER OBJECT
        glTranslate(tx/20., ty/20., - zpos)
        glRotate(ry, 1, 0, 0)
        glRotate(rx, 0, 1, 0)
        Car()
        #increase all itera number
        for i in range(len(iteraList)):
            iteraList[i] = iteraList[i] + 0.01
        if (loopitera % 10) == 0:
            if (loopitera > (250 * knalpotspeed)):
                iteraList.pop(0)
            iteraList.append(0)
        
        #add new number
        # iteraList.append(0)
        # print(len(iteraList))
        for itera in iteraList:
            # print itera
            it = 0
            while (it < 1):
                glBegin(GL_TRIANGLES)
                glVertex3fv((-0.1+it, 4.2+itera, -0.5))
                glVertex3fv((-0.2+it, 4.2+itera, -0.5))
                #   print loopitera
                glVertex3fv((-0.15+it, 4.3+itera, -0.5))
                glEnd()
                glBegin(GL_TRIANGLES)
                glVertex3fv((-0.1+it, 4.2+itera, -0.5))
                glVertex3fv((-0.2+it, 4.2+itera, -0.5))
                #   print loopitera
                glVertex3fv((-0.15+it, 4.25+itera, -0.4))
                glEnd()
                glBegin(GL_TRIANGLES)
                glVertex3fv((-0.1+it, 4.2+itera, -0.5))
                glVertex3fv((-0.15+it, 4.25+itera, -0.4))
                #   print loopitera
                glVertex3fv((-0.15+it, 4.3+itera, -0.5))
                glEnd()
                glBegin(GL_TRIANGLES)
                glVertex3fv((-0.15+it, 4.25+itera, -0.4))
                glVertex3fv((-0.2+it, 4.2+itera, -0.5))
                #   print loopitera
                glVertex3fv((-0.15+it, 4.3+itera, -0.5))
                glEnd()
                it = it + 0.2
        loopitera += knalpotspeed
        if len(iteraList) == 100:
            iteraList = []
        # itera = itera + 0.01
            
        pygame.display.flip()




if __name__ == '__main__':
    mainMobil()
