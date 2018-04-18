# Basic OBJ file viewer. needs objloader from:
#  http://www.pygame.org/wiki/OBJFileLoader
# LMB + move: rotate
# RMB + move: pan
# Scroll wheel: zoom in/out
import sys, pygame
from pygame.locals import *
from pygame.constants import *
from OpenGL.GL import *
from OpenGL.GLU import *
from pgu import gui

# IMPORT OBJECT LOADER
from objloader import *

def mainMobil(red):
  
  pygame.init()
  viewport = (800,600)
  hx = viewport[0]/2
  hy = viewport[1]/2
  srf = pygame.display.set_mode(viewport, OPENGL | DOUBLEBUF)

  glLightfv(GL_LIGHT0, GL_POSITION,  (0, -1, 0, 0.0))
  glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
  glLightfv(GL_LIGHT0, GL_DIFFUSE, (float(red[0]) / 256, float(red[1]) / 256, float(red[2]) / 256, 1.0))
#   glLightfv(GL_LIGHT0, GL_SPECULAR, (float(red[0]) / 256, float(red[1]) / 256, float(red[2]) / 256, 1.0))
#   glLightfv(GL_LIGHT0, GL_SPECULAR, (1, 0.01, 0.01, 1.0))
  glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION,  (0, -300, 0, 0.0))
  glLightfv(GL_LIGHT0, GL_SPOT_CUTOFF,  10)
#   glLightfv(GL_LIGHT0, GL_SPOT_EXPONENT,  100)
#   glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
  
  glEnable(GL_LIGHT0)
#   glLightfv(GL_LIGHT1, GL_POSITION,  (400, 100, 100, 0.0))
#   glLightfv(GL_LIGHT1, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
#   glLightfv(GL_LIGHT1, GL_DIFFUSE, (float(red[0]) / 256, float(red[1]) / 256, float(red[2]) / 256, 1.0))
#   glEnable(GL_LIGHT1)
  glEnable(GL_LIGHTING)
  glEnable(GL_COLOR_MATERIAL)
  glEnable(GL_DEPTH_TEST)
  glShadeModel(GL_SMOOTH)           # most obj files expect to be smooth-shaded

  # LOAD OBJECT AFTER PYGAME INIT
  obj = OBJ(sys.argv[1], swapyz=True)

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

      # RENDER OBJECT
      glTranslate(tx/20., ty/20., - zpos)
      glRotate(ry, 1, 0, 0)
      glRotate(rx, 0, 1, 0)
      glCallList(obj.gl_list)

      pygame.display.flip()



class ColorDialog(gui.Dialog):
    def __init__(self,value,**params):
        self.value = list(gui.parse_color(value))
        
        title = gui.Label("Color Picker")
        
        main = gui.Table()
        
        main.tr()
        
        self.color = gui.Color(self.value,width=64,height=64)
        main.td(self.color,rowspan=3,colspan=1)
        
        ##The sliders CHANGE events are connected to the adjust method.  The 
        ##adjust method updates the proper color component based on the value
        ##passed to the method.
        ##::
        main.td(gui.Label(' Red: '),1,0)
        e = gui.HSlider(value=self.value[0],min=0,max=255,size=32,width=128,height=16)
        e.connect(gui.CHANGE,self.adjust,(0,e))
        main.td(e,2,0)
        ##

        main.td(gui.Label(' Green: '),1,1)
        e = gui.HSlider(value=self.value[1],min=0,max=255,size=32,width=128,height=16)
        e.connect(gui.CHANGE,self.adjust,(1,e))
        main.td(e,2,1)

        main.td(gui.Label(' Blue: '),1,2)
        e = gui.HSlider(value=self.value[2],min=0,max=255,size=32,width=128,height=16)
        e.connect(gui.CHANGE,self.adjust,(2,e))
        main.td(e,2,2)
        
        e = gui.Button("run program")
        main.td(e,1,3)
        e.connect(gui.CLICK,mainMobil,self.value)                
        gui.Dialog.__init__(self,title,main)
        
    ##The custom adjust handler.
    ##::
    def adjust(self,value):
        (num, slider) = value
        # print slider.value
        self.value[num] = slider.value
        self.color.repaint()
        self.send(gui.CHANGE)
    ##

if __name__ == '__main__':
    app = gui.Desktop()
    app.connect(gui.QUIT,app.quit,None)
    
    c = gui.Table(width=640,height=480)
    
    dialog = ColorDialog("#00ffff")
            
    e = gui.Button("Mobil Kelompok Eki")
    e.connect(gui.CLICK,dialog.open,None)
    
    c.tr()
    c.td(e)
    
    app.run(c)
