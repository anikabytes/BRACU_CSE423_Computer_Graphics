from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import time 

# for coodinates storing during right mouse click 
coordinates_arr = []

# for radius of circle 
radius = 30  

# for pause 
pause_flag = False 
pause_arr  = []


# for window screen 
width, height = 500,500

# for radius increment 
increase_radius = 5  
start = time.time()
speed = 0.2



def midPointCircle(x,y,r):

    glPointSize(3)
    glColor3f(1, 0, 0)
    glBegin(GL_POINTS)
    x_p = 0
    y_p = r
    d = 1 - r

    while x_p <= y_p:


        glVertex2f(x_p + x, y_p + y)
        glVertex2f(-x_p + x, y_p + y)
        glVertex2f(x_p + x, -y_p + y)
        glVertex2f(-x_p + x, -y_p + y)
        glVertex2f(y_p+ x, x_p + y)
        glVertex2f(-y_p + x, x_p + y)
        glVertex2f(y_p + x, -x_p + y)
        glVertex2f(-y_p + x, -x_p + y)

        forSE = 2*(x_p-y_p)+5
        forE = (2*x_p) +3 

        
        if d >= 0:
            x_p += 1
            y_p -= 1
            d += forSE
        else:
            x_p += 1
            d += forE

    glEnd()

    
def mouseListener(button, state, x, y):

    global radius

    if pause_flag == False: 
        if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
            create_x,create_y = x - width / 2, height / 2 - y
            coordinates_arr.append((create_x,create_y))
    
        glutPostRedisplay()

def keyboardListener(key, x, y):

    global pause_flag, pause_arr

    if key == b' ':
        pause_arr.append(1)
    
    if (len(pause_arr)==1) :
        print("Pause")
        pause_flag = True 
    else :
        print("Start")
        pause_flag = False 
        pause_arr.clear()

    glutPostRedisplay()

def specialKeyListener(key,x,y) :

    global speed 

    if (pause_flag == False) : 
        if (key==GLUT_KEY_RIGHT) :
            speed *= 2
        if (key==GLUT_KEY_LEFT) :
            speed /= 2
        
        print("Radius increases by:",speed)
    

    glutPostRedisplay()

def animation() :
    glutPostRedisplay()


def iterate() :
    glViewport(0,0,width,height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-width / 2, width / 2, -height / 2, height / 2)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def showScreen() :
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()

    global start, radius

    end = time.time()
    duration = end - start  

    if pause_flag == False : 
        radius += increase_radius * duration * speed 
        start = end 

    for coordinate in coordinates_arr:
        x, y = coordinate
        if (-width / 2 + radius < x < width / 2 - radius) and (-height / 2 + radius < y < height / 2 - radius):
                midPointCircle(x, y, radius)
    
    
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(width,height)
glutInitWindowPosition(0,0)
wind = glutCreateWindow(b"Midpoint Circle Algo")
glutDisplayFunc(showScreen)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glutIdleFunc(animation)
glutMainLoop()


