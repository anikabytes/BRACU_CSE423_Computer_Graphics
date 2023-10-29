from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random 

bg = (0.0,0.0,0.0,0.0)
angle = 0.0
raindrop_arr = []

def raindrop(x1,y1): # create raindrop # Task 1 (i)
    glColor3f(0.0,0.0,1.0)
    glPointSize(3)
    glBegin(GL_POINTS)
    glVertex2f(x1,y1)
    glEnd()

def rain_drops() : # Task 1 (i)
    
    global angle 
    for i in range(0,len(raindrop_arr)) :
        update_x, update_y = raindrop_arr[i] 
        #update the raindrop coordinate wrt angle 
        update_x += angle 
        update_y -= 1

        # avoid the raindrop enterting the house 
        if (update_y < 250) or (120<update_x<380 and 100<update_y<300) :
            update_x = random.uniform(100,400)
            update_y = random.uniform(200,500)
        raindrop_arr[i] = (update_x,update_y)


def draw_house(): # Task 1 (i)

    glColor3f(0.0, 0.0, 1.0) 
    glPointSize(5) 
    glLineWidth(5)
    glColor3f(1.0,0.0,0.0)
    glBegin(GL_LINES)

    #roof 
    glVertex2f(400,300)
    glVertex2f(100,300)
    glVertex2f(400,300)
    glVertex2f(250,400)
    glVertex2f(100,300)
    glVertex2f(250,400)

    #body
    glVertex2f(380,300)
    glVertex2f(380,100)
    glVertex2f(120,300)
    glVertex2f(120,100)
    glVertex2f(120,100)
    glVertex2f(380,100)
    glEnd()

    glPointSize(5)
    glLineWidth(2)
    glBegin(GL_LINES)

    # door 
    glVertex2f(140,100) 
    glVertex2f(140,200)
    glVertex2f(200,100)
    glVertex2f(200,200)
    glVertex2f(140,200)
    glVertex2f(200,200)

    #window 
    glVertex2f(350,200)
    glVertex2f(350,250)
    glVertex2f(300,200)
    glVertex2f(300,250)
    glVertex2f(350,250)
    glVertex2f(300,250)
    glVertex2f(350,200)
    glVertex2f(300,200)
    glVertex2f(300,225)
    glVertex2f(350,225)
    glVertex2f(325,250)
    glVertex2f(325,200)
    glEnd()

    glPointSize(5)
    glBegin(GL_POINTS)
    # door lock 
    glVertex2f(190,120)
    glEnd()



def specialKeyListener(key, x, y): # Task 1 (ii)
    global angle 
    if key==GLUT_KEY_RIGHT:
        angle += 0.5
        print("Tilt Right")
    if key== GLUT_KEY_LEFT:		
        angle -= 0.5
        print("Tilt Left")
    
    glutPostRedisplay()

def keyboardListener(key, x, y): # Task 1 (iii)
    global bg

    if (key == b'n'): 
        bg = (0.0,0.0,0.0,0.0)
        print("It's night")
    if (key == b'm'):
        bg = (1.0,1.0,1.0,1.0)
        print("It's morning")
        
    
    glutPostRedisplay()

def animation() :
    rain_drops()
    glutPostRedisplay()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():

     # Set the background color
    glClearColor(*bg)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    draw_house()

    # call the raindrop function 
    for k in raindrop_arr :
        raindrop(k[0],k[1])
    glutSwapBuffers()





glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice") #window name
glutDisplayFunc(showScreen)
glutKeyboardFunc(keyboardListener)
#glutMouseFunc(mouseListener)
glutIdleFunc(animation)
glutSpecialFunc(specialKeyListener)

# random raindrop coordinate is stored in raindrop_arr
for j in range(100):
    x2 = random.uniform(100,400)
    y2= random.uniform(200,500)
    raindrop_arr.append((x2, y2))



glutMainLoop()