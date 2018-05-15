import pygame
import math
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

angle = 0.0

verticies = (
    (0.2, 0.4,0.6,1),
    (0.6, 0.5,0.6,1),
    (0.6, 0.5,0.2,1),
    (0.2,0.4,0.2,1),
    (0.2,0.2,0.6,1),
    (0.3, -1, 1,1),
    (0.6,0.2,0.6,1),
    (0.6,0.2,0.2,1),
    (0.2,0.2,0.2,1),
    (0.2,0.2,0.6,1),
    (0.2, 0.4,0.6,1),
    (0.2,0.4,0.2,1),
    (0.2,0.2,0.2,1),
    (0.6,0.2,0.6,1),

    (0.6,0.5,0.6,1),
    (0.6,0.5,0.2,1),
    (0.6,0.2,0.2,1),
    (0.2,0.2,0.6,1),
    (0.6,0.2,0.6,1),
    (0.6,0.5,0.6,1),
    (0.2,0.4,0.6,1),
    (0.2,0.2,0.2,1),
    (0.6,0.2,0.2,1),
    (0.6,0.5,0.2,1),
    (0.2,0.4,0.2,1),
    (0.7,0.65,0.6,1),
    (0.7,0.65,0.2,1),
    (1.7,0.65,0.2,1),

    (1.7,0.65,0.6,1),
    (1.8, 0.5,0.6,1),
    (1.8, 0.5,0.2,1),
    (2.1, 0.4, 0.2,1),
    (2.1,0.4,0.6,1),
    (2.1,0.2,0.6,1),

    (2.1,0.2,0.2,1),
    (-0.3, -0.5, -1,1),
    (0.3, -0.5, -1,1),
    (0.6, -0.5, -1,1),
    (1, -0.5, -1,1),
    (1, 0, -1,1),
    )

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

def Car():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
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

def compute_location(user_theta, user_height):
    x = 2 * math.cos(user_theta)
    y = 2 * math.sin(user_theta)
    z = user_height
    d = math.sqrt(x * x + y * y + z * z)

    # Set matrix mode
    glMatrixMode(GL_MODELVIEW)

    # Reset matrix
    glLoadIdentity()
    glFrustum(-d * 0.5, d * 0.5, -d * 0.5, d * 0.5, d - 1.1, d + 1.1)

    # Set camera
    gluLookAt(x, y, z, 0, 0, 0, 0, 0, 1)

def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL | pygame.OPENGLBLIT)  


    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    glTranslatef(-0.7,0.0, -4)

    glRotatef(0,0,0,0)
    glEnable(GL_DEPTH_TEST)
    glDepthMask(GL_TRUE)
    glDepthFunc(GL_LEQUAL)
    # Radius of sphere
    # radius = radius

    # Number of latitudes in sphere
    lats = 100

    # Number of longitudes in sphere
    longs = 100

    user_theta = -2
    user_height = 2

    # Direction of light
    direction = [0.2, 0.4,0.6, 0.6]

    # Intensity of light
    intensity = [1, 1, 1, 1.0]

    # Intensity of ambient light
    ambient_intensity = [0.5, 0.5, 0.5, 1.0]

    # The surface type(Flat or Smooth)
    surface = GL_FLAT

    compute_location(user_theta, user_height)    

    # Enable lighting
    glEnable(GL_LIGHTING)

    # Set light model
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient_intensity)

    # Enable light number 0
    glEnable(GL_LIGHT0)

    # Set position and intensity of light
    glLightfv(GL_LIGHT0, GL_POSITION, direction)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, intensity)

    # Setup the material
    glEnable(GL_COLOR_MATERIAL)
    glColorMaterial(GL_FRONT, GL_AMBIENT_AND_DIFFUSE)

    while True:        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glRotatef(2, 0, -1, 0)
                    user_theta -= 0.1
                if event.key == pygame.K_RIGHT:
                    glRotatef(2, 0 , 1, 0)
                    user_theta += 0.1
                if event.key == pygame.K_UP:
                    glRotatef(2, 1, 0, 0)
                    user_height += 0.1
                if event.key == pygame.K_DOWN:
                    glRotatef(2, -1, 0, 0)
                    user_height -= 0.1
        # glRotatef(3,0,1,0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        pygame.time.wait(10)

        glDepthRange(0.0, 1.0)

        Car()
        # user_theta -= 0.1
        compute_location(user_theta, user_height)
        pygame.display.flip()

        pygame.time.wait(10)


main()
