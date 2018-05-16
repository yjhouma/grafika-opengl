import sys, pygame, math
import timeit
from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *
import random

class Particle():
    def __init__(self, startx, starty, startz, col):
        self.x = startx
        self.y = starty
        self.z = startz
        self.col = col
        self.sx = startx
        self.sy = starty
        self.sz = startz

    def move(self):
        if self.y > 1:
            self.x=self.sx
            self.y=self.sy
            self.z=self.sz

        else:
            self.y+=random.uniform(0.02, 0.07)

        self.x+=random.uniform(0.01, 0.05)
        # self.z+=random.uniform(-0.1, 0.1)


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


def draw_circle(cx, cy, r, num_segments, filled):
    theta = 2 * 3.1415926 / num_segments
    c = math.cos(theta)
    s = math.sin(theta)

    x = r
    y = 0

    if filled:
        mode = GL_POLYGON
    else:
        mode = GL_LINE_LOOP

    glBegin(mode)

    for ii in range(0,num_segments):
        glVertex3f(x+cx, y+cy, 0.3)

        # apply the rotation
        t = x
        x = c*x-s*y
        y = s*t+c*y

    glEnd()

def main():
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
    glEnableClientState (GL_VERTEX_ARRAY)
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

    raindrops = []
    raining = -1
    rainspeed = float(red[3]) / 2550
    while raining < 1 :
        raindrops.append([raining, random.uniform(-1,1)])
        raining += 0.03

    smoke = []
    for i in range(75):
        smoke.append(Particle(2.25,0.2,-10.3, (255,255,255)))

    while 1:
        start = timeit.default_timer()
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

        for hujan in range(len(raindrops)):
            glBegin(GL_QUADS)
            glColor3f(255,255,255)
            glVertex3f(raindrops[hujan][0] + 0.005  ,raindrops[hujan][1] + 0.05,-1)
            glVertex3f(raindrops[hujan][0] + 0.005  ,raindrops[hujan][1],-1)
            glVertex3f(raindrops[hujan][0]         ,raindrops[hujan][1],  -1)
            glVertex3f(raindrops[hujan][0]         ,raindrops[hujan][1] + 0.05,-1)
            glEnd()
            raindrops[hujan][1] -= rainspeed
            if raindrops[hujan][1] < -1:
                raindrops[hujan][1] = 1
        # RENDER OBJECT
        glTranslate(tx/20., ty/20., - zpos)
        glRotate(ry, 1, 0, 0)
        glRotate(rx, 0, 1, 0)
        Car()

        for p in smoke:
            p.move()
            glColor3f(30,30,30)
            draw_circle(p.x, p.y, 0.015, 100, True)

        pygame.display.flip()
        print(round(1/(-start+timeit.default_timer())))

if __name__ == '__main__':
    main()
