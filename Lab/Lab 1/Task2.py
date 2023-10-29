from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random 

array = []
constant = 0.01
freeze_constant = 0 
speed_x = random.uniform(0.1,0.5)
speed_y = random.uniform(0.1,0.5)
blink = False 
freeze = False 
freeze_arr = []
blink_arr = []


def draw_points(x,y,color) : # Task 2 (i)

    #drawing the points when right button is pressed 
    glPointSize(5)
    glBegin(GL_POINTS)
    glColor3f(color[0],color[1],color[2])
    glVertex2f(x,y)
    glEnd()

def update_point() : # Task 2 (i)

    global constant, freeze_constant  

    # updating the points to adjust their speed for animation 
    for find in array :
        if (freeze == False) : 
            find['x'] += (constant * speed_x)
            find['y'] += ( constant * speed_y)
        else :
            find['x'] += (freeze_constant * speed_x)
            find['y'] += (freeze_constant * speed_y)

def generate_point() : # Task 2 (i)
    x = random.uniform(100,400)
    y = random.uniform(100,400)
    return x,y

def generate_color() : # Task 2 (i)
    return [random.random(),random.random(),random.random()]


def mouseListener(button,state,x,y) :

    global blink, freeze

    if (freeze == False) : 
        if (button==GLUT_RIGHT_BUTTON) and (state==GLUT_DOWN) : # Task 2 (i)
            blink = False 
            print("point created")
            create_x, create_y = generate_point()
            #print(create_x,create_y)
            fix_color = generate_color()
            #print(fix_color)
            array.append({'x':create_x,'y':create_y, 'color':fix_color})
        
        if (button==GLUT_LEFT_BUTTON) and (state==GLUT_DOWN) : # Task 2 (iii)
            blink = True 
            print("Blink!")
        glutPostRedisplay()


def specialKeyListener(key,x,y) : # Task 2 (ii)

    global constant 

    if (freeze == False) : 
        if (key==GLUT_KEY_UP) :
            #speed_x *= 2 
            #speed_y *= 2  
            constant *= 2 

            print("Speed increased by",constant)
            
        if (key==GLUT_KEY_DOWN) :
            #speed_x /= 2 
            #speed_y /= 2 
            constant /= 2
            print("Speed decreased by",constant)
    

    glutPostRedisplay()

def keyBoardListener(key,x,y) : # Task 2 (iv)

    global freeze, freeze_arr

    if (key==b' ') :
        freeze_arr.append("Freeze!!!")
    
    if (len(freeze_arr) == 1 ) :
        print("Freeze!!!")
        freeze = True 
    else :
        print("UnFreeze!!!")
        freeze = False 
        freeze_arr.clear()
    #print(freeze_arr)
    
    glutPostRedisplay()


def animation(): # Task 2 (i)

    global freeze 
    if (freeze == False): 
        update_point()
    else :
        pass 

    glutPostRedisplay()
  

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()


def showScreen():

    glClearColor(0,0,0,0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    #draw_points()

    for pick in array : # setting x,y,color for the draw_points from the array of points info 
        take_x = pick['x']
        take_y = pick['y']
        if (blink == False) :
            color = pick['color']
        else :
            color = [0.0,0.0,0.0]
        
        draw_points(take_x,take_y,color)

    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)
glutMouseFunc(mouseListener)
glutSpecialFunc(specialKeyListener)
glutKeyboardFunc(keyBoardListener)
glutIdleFunc(animation)
glutMainLoop()
