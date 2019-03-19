from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
from math import *

def circle(r=1,x1=0,y1=0,R=0,G=0,B=0): #B and F to control the Circle
    glBegin(GL_POINTS)
    glColor3f(R,G,B)
    for theta in np.arange(0,360,.01):
        x=r*cos(theta)+x1
        y=r*sin(theta)+y1
        glVertex(x,y,0)

    glEnd()     

def fcircle(r=1,x1=0,y1=0 ,R=0,G=0,B=0):
    glBegin(GL_POLYGON)
    glColor3f(R,G,B)
    for theta in np.arange(0,360,.01):
           x=r*cos(theta)+x1
           y=r*sin(theta)+y1
           glVertex(x,y,0)

    glEnd()  
    
def display():
    Axis()
    
    glBegin(GL_POLYGON)
    glColor3f(.6,.6,.6)
    glVertex(.22,-.3,0)
    glVertex(.6,-.3,0)
    glVertex(.6,-.35,0)
    glVertex(.348,-.555,0)
    glVertex(.22,-.555,0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0,0,0)
    glVertex(.22,-.3,0)
    glVertex(.6,-.3,0)
    glVertex(.6,-.35,0)
    glVertex(.348,-.555,0)
    glVertex(.22,-.555,0)
    
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(.6,.6,.6)
    glVertex(-.22,-.3,0)
    glVertex(-.6,-.3,0)
    glVertex(-.6,-.35,0)
    glVertex(-.348,-.555,0)
    glVertex(-.22,-.555,0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0,0,0)
    glVertex(-.22,-.3,0)
    glVertex(-.6,-.3,0)
    glVertex(-.6,-.35,0)
    glVertex(-.348,-.555,0)
    glVertex(-.22,-.555,0)
    
    glEnd()

    
    glBegin(GL_POLYGON)
    glColor3f(1,0.8,0.1)
    glVertex(-.4,-.4,0)
    glVertex(-.4,.4,0)
    glVertex(.4,.4,0)
    glVertex(.4,-.4,0)
    glEnd()
    
    glBegin(GL_LINE_LOOP)
    glColor3f(0,0,0)
    glVertex(-.4,-.4,0)
    glVertex(-.4,.4,0)
    glVertex(.4,.4,0)
    glVertex(.4,-.4,0)
    glEnd()    

    glBegin(GL_POLYGON)
    glColor3f(0.9,0.9,0.5)
    glVertex(-.04,.4,0)
    glVertex(-.04,.5,0)
    glVertex(.04,.5,0)
    glVertex(.04,.4,0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.9,0.9,0.5)
    glVertex(-.04,.5,0)
    glVertex(-.13,.6,0)
    glVertex(.13,.6,0)
    glVertex(.04,.5,0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0,0,0)
    glVertex(-.04,.4,0)
    glVertex(-.04,.5,0)
    glVertex(.04,.5,0)
    glVertex(.04,.4,0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0,0,0)
    glVertex(-.04,.5,0)
    glVertex(-.13,.6,0)
    glVertex(.13,.6,0)
    glVertex(.04,.5,0)
    glEnd()

    #Eyes
    
    fcircle(.07,.10,.6,1,1,1)
    fcircle(.07,-.10,.6,1,1,1)
    circle(.07,-.10,.6)
    circle(.07,.10,.6)
    fcircle(.03,.13,.6,.1,.2,.8)
    fcircle(.03,-.07,.6,.1,.2,.8)

    fcircle(.02,.13,.6)
    fcircle(.02,-.07,.6)

    glBegin(GL_POLYGON)
    glColor3f(1,1,0.4)
    glVertex(-.35,-.3,0)
    glVertex(-.35,.3,0)
    glVertex(0,.3,0)
    glVertex(0,-.3,0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0,0.2,1)
    glVertex(-.28,.35,0)
    glVertex(-.28,.38,0)
    glVertex(-.12,.38,0)
    glVertex(-.12,.35,0)
    glEnd()
    
    glBegin(GL_LINE_LOOP)
    glColor3f(0,0,0)
    glVertex(-.28,.35,0)
    glVertex(-.28,.38,0)
    glVertex(-.12,.38,0)
    glVertex(-.12,.35,0)
    glEnd()    
    
    fcircle(.02,.24,.37,1,.2,.1)
    circle(.02,.24,.37)
    
    glBegin(GL_LINE_LOOP)
    glColor3f(0,0,0)
    glVertex(-.38,.33,0)
    glVertex(-.38,.4,0)
    glVertex(.38,.4,0)
    glVertex(.38,.33,0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0,0,0)
    glVertex(.27,.4,0)
    glVertex(.27,.34,0)
    glVertex(.21,.34,0)
    glVertex(.21,.4,0)
    glEnd()

    #RightARM
    glBegin(GL_POLYGON)
    glColor3f(.6,.6,.6)
    glVertex(.18,.02,0)
    glVertex(.18,.06,0)
    glVertex(.45,.06,0)
    glVertex(.45,.02,0)
    glEnd()
    glBegin(GL_LINE_LOOP)
    glColor3f(0,0,0)
    glVertex(.18,.02,0)
    glVertex(.18,.06,0)
    glVertex(.45,.06,0)
    glVertex(.45,.02,0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(.6,.6,.6)
    glVertex(.18,.14,0)
    glVertex(.18,.18,0)
    glVertex(.45,.18,0)
    glVertex(.45,.14,0)
    glEnd()
    glBegin(GL_LINE_LOOP)
    glColor3f(0,0,0)
    glVertex(.18,.14,0)
    glVertex(.18,.18,0)
    glVertex(.45,.18,0)
    glVertex(.45,.14,0)
    glEnd()


    
    glBegin(GL_POLYGON)
    glColor3f(.6,.6,.6)
    glVertex(.4,0,0)
    glVertex(.4,.2,0)
    glVertex(.53,.2,0)
    glVertex(.53,0,0)
    glEnd()
    glBegin(GL_LINE_LOOP)
    glColor3f(0,0,0)
    glVertex(.4,0,0)
    glVertex(.4,.2,0)
    glVertex(.53,.2,0)
    glVertex(.53,0,0)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0,0,0)
    glVertex(.3,.02,0)
    glVertex(.3,.06,0)
    glVertex(.3,.14,0)
    glVertex(.3,.18,0)
    glEnd()

    #LeftARM
    glBegin(GL_POLYGON)
    glColor3f(.6,.6,.6)
    glVertex(-.18,.02,0)
    glVertex(-.18,.06,0)
    glVertex(-.45,.06,0)
    glVertex(-.45,.02,0)
    glEnd()
    glBegin(GL_LINE_LOOP)
    glColor3f(0,0,0)
    glVertex(-.18,.02,0)
    glVertex(-.18,.06,0)
    glVertex(-.45,.06,0)
    glVertex(-.45,.02,0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(.6,.6,.6)
    glVertex(-.18,.14,0)
    glVertex(-.18,.18,0)
    glVertex(-.45,.18,0)
    glVertex(-.45,.14,0)
    glEnd()
    glBegin(GL_LINE_LOOP)
    glColor3f(0,0,0)
    glVertex(-.18,.14,0)
    glVertex(-.18,.18,0)
    glVertex(-.45,.18,0)
    glVertex(-.45,.14,0)
    glEnd()


    
    glBegin(GL_POLYGON)
    glColor3f(.6,.6,.6)
    glVertex(-.4,0,0)
    glVertex(-.4,.2,0)
    glVertex(-.53,.2,0)
    glVertex(-.53,0,0)
    glEnd()
    glBegin(GL_LINE_LOOP)
    glColor3f(0,0,0)
    glVertex(-.4,0,0)
    glVertex(-.4,.2,0)
    glVertex(-.53,.2,0)
    glVertex(-.53,0,0)
    glEnd()

    glBegin(GL_LINES)
    glColor3f(0,0,0)
    glVertex(-.3,.02,0)
    glVertex(-.3,.06,0)
    glVertex(-.3,.14,0)
    glVertex(-.3,.18,0)
    glEnd()

    #Right-LEG

    glBegin(GL_POLYGON)
    glColor3f(.6,.6,.6)
    glVertex(.3,-.58,0)
    glVertex(.555,-.58,0)
    glVertex(.555,-.6,0)
    glVertex(.3,-.6,0)    
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0,0,0)
    glVertex(.3,-.58,0)
    glVertex(.555,-.58,0)
    glVertex(.555,-.6,0)
    glVertex(.3,-.6,0)    
    glEnd()

    
    glBegin(GL_POLYGON)
    glColor3f(.6,.6,.6)
    glVertex(.5,-.25,0)
    glVertex(.7,-.25,0)
    glVertex(.7,-.65,0)
    glVertex(.5,-.65,0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0,0,0)
    glVertex(.5,-.25,0)
    glVertex(.7,-.25,0)
    glVertex(.7,-.65,0)
    glVertex(.5,-.65,0)
    glEnd()

    for i in np.arange(-.25,-.65,-.05):
        glBegin(GL_LINES)
        glColor3f(0,0,0)
        glVertex(.5,i,0)
        glVertex(.7,i,0)
        glEnd()
        
    '''
    
    '''
    glBegin(GL_POLYGON)
    glColor3f(.6,.6,.6)
    glVertex(.348,-.555,0)
    glVertex(.22,-.555,0)
    glVertex(.22,-.625,0)
    glVertex(.348,-.625,0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0,0,0)
    glVertex(.348,-.555,0)
    glVertex(.22,-.555,0)
    glVertex(.22,-.625,0)
    glVertex(.348,-.625,0)
    glEnd()


    #LeftLeg
    glBegin(GL_POLYGON)
    glColor3f(.6,.6,.6)
    glVertex(-.3,-.58,0)
    glVertex(-.555,-.58,0)
    glVertex(-.555,-.6,0)
    glVertex(-.3,-.6,0)    
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0,0,0)
    glVertex(-.3,-.58,0)
    glVertex(-.555,-.58,0)
    glVertex(-.555,-.6,0)
    glVertex(-.3,-.6,0)    
    glEnd()
    
    glBegin(GL_POLYGON)
    glColor3f(.6,.6,.6)
    glVertex(-.5,-.25,0)
    glVertex(-.7,-.25,0)
    glVertex(-.7,-.65,0)
    glVertex(-.5,-.65,0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0,0,0)
    glVertex(-.5,-.25,0)
    glVertex(-.7,-.25,0)
    glVertex(-.7,-.65,0)
    glVertex(-.5,-.65,0)
    glEnd()

    for i in np.arange(-.25,-.65,-.05):
        glBegin(GL_LINES)
        glColor3f(0,0,0)
        glVertex(-.5,i,0)
        glVertex(-.7,i,0)
        glEnd()
        
    '''
    
    '''
    glBegin(GL_POLYGON)
    glColor3f(.6,.6,.6)
    glVertex(-.348,-.555,0)
    glVertex(-.22,-.555,0)
    glVertex(-.22,-.625,0)
    glVertex(-.348,-.625,0)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor3f(0,0,0)
    glVertex(-.348,-.555,0)
    glVertex(-.22,-.555,0)
    glVertex(-.22,-.625,0)
    glVertex(-.348,-.625,0)
    glEnd()




    

    
    
    glFlush()
    
def Axis():
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
    '''glColor3f(0,0,1)
    glBegin(GL_LINES)
    glVertex(-1 , 0 ,0)
    glVertex(1,0,0)
    
    glColor3f(0,1,0)
    glVertex(0 , -1 ,0)
    glVertex(0,1,0)

    glEnd()
    '''
    
    
    #glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(700,700)
glutCreateWindow(b"Walle")
glutDisplayFunc(display)
#myinit()
glutMainLoop()
