from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import numpy as np
from math import *

Angle=0
x=0
forward=True
def myinit():
    glMatrixMode(GL_PROJECTION)
    gluPerspective(60 , 1 , .1 ,60)
    gluLookAt(8,9,10,
              0,0,0,
              0,1,0)
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
    
def display():
    global Angle
    global x
    global forward
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glColor3f(.8,.8,.8)
    glScale(1,.25,.5)
    glTranslate(x,0,0)
    glutSolidCube(5)
    
    glLoadIdentity()
    glColor3f(.2,.2,.2)
    glTranslate(x,5*.25,0)
    glScale(.5,.25,.5)
    glutSolidCube(5)


    glLoadIdentity()
    glColor3f(.2,.2,.2)
    glTranslate(2.5+x , -2.5*.25 , 2.5*.5)
    glRotate(Angle , 0 , 0 ,1)
    glutSolidTorus(.2 , .5 , 12 , 8)
    glLoadIdentity()
    glColor3f(.2,.2,.2)
    glTranslate(2.5+x , -2.5*.25 , -2.5*.5)
    glRotate(Angle , 0 , 0 ,1)
    glutSolidTorus(.2 , .5 , 12 , 8)
    glLoadIdentity()
    glColor3f(.2,.2,.2)
    glTranslate(-2.5+x , -2.5*.25 , 2.5*.5)
    glRotate(Angle , 0 , 0 ,1)
    glutSolidTorus(.2 , .5 , 12 , 8)
    glLoadIdentity()
    glColor3f(.2,.2,.2)
    glTranslate(-2.5+x , -2.5*.25 , -2.5*.5)
    glRotate(Angle , 0 , 0 ,1)
    glutSolidTorus(.2 , .5 , 12 , 8)




    glLoadIdentity()
    glColor3f(1,1,0)
    glTranslate(2.5+x , -2.5*.25 , -2.5*.2)
    glutSolidSphere(.3 , 12 , 8)
    glLoadIdentity()
    glColor3f(1,1,0)
    glTranslate(2.5+x , -2.5*.25 , 2.5*.2)
    glutSolidSphere(.3, 12 , 8)

    glLoadIdentity()
    glColor3f(.5,.5,.5)
    glBegin(GL_POLYGON)
    glVertex(25 , -1.5 , 3)
    glVertex(25 , -1.5 , -3)
    glVertex(-30 , -1.5 , -3)
    glVertex(-30 , -1.5 , 3)
    glEnd()

    glLoadIdentity()
    glColor3f(.2,.5,.1)
    glBegin(GL_POLYGON)
    glVertex(25 , -1.5 , 50)
    glVertex(25 , -1.5 , 3)
    glVertex(-30 , -1.5 , 3)
    glVertex(-30 , -1.5 , 50)
    glEnd()

    glLoadIdentity()
    glColor3f(.2,.5,.1)
    glBegin(GL_POLYGON)
    glVertex(25 , -1.5 , -3)
    glVertex(25 , -1.5 , -50)
    glVertex(-40 , -1.5 , -50)
    glVertex(-40 , -1.5 , -3)
    glEnd()
    
    glLoadIdentity()
    glColor3f(.2,.2,.5)
    glBegin(GL_POLYGON)
    glVertex(25 , -2 , -25)
    glVertex(-40 , -2 , -10)
    glVertex(-40 , 40 , -10)
    glVertex(25 , 40 , -25)
    glEnd()
    for i in range ( 10,-35,-5):
       glLoadIdentity()
       glColor3f(.5,.3,0)
       glTranslate(i,0,-7)
       glScale(.25,2,.25)
       glutSolidCube(2.5)

       glLoadIdentity()
       glColor3f(.2,.55,.1)
       glTranslate(i,2,-7)
       glRotate(-90,1,0,0)
       glutSolidCone(2,3,15,15)
    
    if forward:
        Angle-=.1
        x+=.01
        if x>6:
            forward = False
    else:
        Angle+=.1
        x-=.01
        if x<-10:
            forward = True
         
    glutSwapBuffers()
    
def Axis():
    glClearColor(1,1,1,1)
    glColor3f(1,0,0)
    glBegin(GL_LINES)
    glVertex(0 , 0 ,0)
    glVertex(20,0,0)
    
    glColor3f(0,1,0)
    glVertex(0 , 0 ,0)
    glVertex(0,20,0)

    glColor3f(0,0,1)
    glVertex(0 , 0 ,0)
    glVertex(0,0,20)
    glEnd()

    
    
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB |GLUT_DEPTH)
glutInitWindowSize(700,700)
glutCreateWindow(b"moving car")
glutDisplayFunc(display)
myinit()
Axis()
glutIdleFunc(display)
glutMainLoop()
