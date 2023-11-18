from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random


# for catcher
x1,x2,x3,x4 = 20,50,200,230
y1,y2 = 10,50
catcher_rec = [(x1, y2), (x4, y1)]


# for diamond
x5,x6,x7 = 200,210,220
y3,y4,y5 = 300,325,350
diamond_arr = []
fall_speed = 2


# for play/pause button & left_arrow button
pause_flag = False #pause
start_flag = False #start again
over_flag = False #game over


# for score count
score_count = 0




def draw_points(x,y) :
    glPointSize(2)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()






def find_zone(x0, y0, x1, y1):


    dx = x1 - x0
    dy = y1 - y0


    zone = -1


    if abs(dx) > abs(dy):  
        if dx > 0 and dy > 0:
            zone = 0
        elif dx < 0 and dy > 0:
            zone = 3
        elif dx < 0 and dy < 0:
            zone = 4
        else:
            zone = 7


    else:                  
        if dx > 0 and dy > 0:
            zone = 1
        elif dx < 0 and dy > 0:
            zone = 2
        elif dx < 0 and dy < 0:
            zone = 5
        else:
            zone = 6
   
    return zone






def convert(original_zone,x,y) :


    if (original_zone == 0) :
        return x,y
    elif (original_zone == 1) :
        return y,x
    elif (original_zone == 2) :
        return -y,x
    elif (original_zone == 3) :
        return -x,y
    elif (original_zone == 4) :
        return -x,-y
    elif (original_zone == 5) :
        return -y,-x
    elif (original_zone == 6) :
        return -y,x
    elif (original_zone == 7) :
        return x,-y






def convert_original(original_zone,x,y) :


    if (original_zone == 0) :
        return x,y
    elif (original_zone == 1) :
        return y,x
    elif (original_zone == 2) :
        return -y,-x
    elif (original_zone == 3) :
        return -x,y
    elif (original_zone == 4) :
        return -x,-y
    elif (original_zone == 5) :
        return -y,-x
    elif (original_zone == 6) :
        return y,-x
    elif (original_zone == 7) :
        return x,-y
   




def midpoint(zone,x0,y0, x1,y1) :


    dx = x1-x0
    dy = y1-y0


    d = (2*dy) - dx


    forE = 2*dy


    forNE = 2*(dy-dx)


    x = x0
    y = y0




    while (x < x1) :


        org_x, org_y = convert_original(zone,x,y)
        draw_points(org_x,org_y)


        if (d<=0) :
            x += 1
            d += forE
        else :
            x += 1
            y += 1
            d += forNE




def eight_way_symmetry(x0,y0,x1,y1) :


    zone = find_zone(x0,y0,x1,y1)
    conv_x0, conv_y0 = convert(zone,x0,y0)
    conv_x1, conv_y1 = convert(zone,x1,y1)
    midpoint(zone,conv_x0,conv_y0,conv_x1,conv_y1)      






def draw_catcher():


    global x1,x2,x3,x4,y1,y2


    glColor3f(1.0,1.0,1.0)
    eight_way_symmetry(x2,y1,x3,y1)
    eight_way_symmetry(x1,y2,x2,y1)
    eight_way_symmetry(x3,y1,x4,y2)
    eight_way_symmetry(x1,y2,x4,y2)








def specialKeyListener(key,x,y) :


    global x1,x2,x3,x4,y1,y2


    move = 10


    if (pause_flag == False) :
        if (key == GLUT_KEY_RIGHT) :
            if (x1<500) and (x2<=500) and (x3<500) and (x4<500)  :
                x1 += move
                x2 += move
                x3 += move
                x4 += move


        if (key==GLUT_KEY_LEFT) :
            if (x1>0) and (x2>0) and (x3>0) and (x4>0) :
                x1 -= move
                x2 -= move
                x3 -= move
                x4 -= move
   
    glutPostRedisplay()



def check_collision(ch_x,ch_y) :

    global score_count,over_flag,flg

    if (ch_y == y2) and ((x3-30 <= ch_x ) or (ch_x < x4)):
        score_count += 1 
        print(f"Score: {score_count}")
    elif (ch_y == y1) and not((x3-30 <= ch_x ) or (ch_x < x4)) :
        print(f"Game Over! Total Score:{score_count}")
        over_flag = True



def draw_diamond(c_x,c_y) :


    global x5,x6,x7,y3,y4,y5

    check_collision(c_x,c_y)



    glColor3f(1.0,0.0,0.5)
    if (x7<500) and (x5>0) and (y5<500) and (y3>0):
        eight_way_symmetry(x5+c_x,y4-c_y,x6+c_x,y5-c_y)
        eight_way_symmetry(x6+c_x,y5-c_y,x7+c_x,y4-c_y)
        eight_way_symmetry(x5+c_x,y4-c_y,x6+c_x,y3-c_y)
        eight_way_symmetry(x6+c_x,y3-c_y,x7+c_x,y4-c_y)
   




def left_arrow() :


    glColor3f(0.0,1.0,1.0)
    eight_way_symmetry(50,425,100,425)
    eight_way_symmetry(70,430,50,425)
    eight_way_symmetry(70,420,50,425)






def cross() :


    glColor3f(1.0,0.0,0.0)
    eight_way_symmetry(400,400,450,450)
    eight_way_symmetry(400,450,450,400)






def play() :


    glColor3f(1.0,1.0,0.0)
    eight_way_symmetry(250,450,250,400)
    eight_way_symmetry(255,450,255,400)


def pause() :


    glColor3f(1.0,1.0,0.0)
    eight_way_symmetry(250,450,250,400)
    eight_way_symmetry(250,450,270,425)
    eight_way_symmetry(250,400,270,425)



def mouseListener(button,state,x,y) :
   
    global pause_flag,x1,x2,x3,x4,score_count,start_flag,over_flag,score_count


    count = 0
    new_y = 500-y


    if (button == GLUT_LEFT_BUTTON) and (state == GLUT_DOWN) :


        if (250<=x<=255) and (400<=new_y<=450):
            count += 1
        if (count%2 !=0) :
            pause_flag = True
            print(f"Pause Score:{score_count}")
           
        if (count%2 == 0) :
            pause_flag = False
           


        if (400<=x<=450) and (400<=new_y<=450) :
            over_flag = True
            print(f"Goodbye! Total Score:{score_count}")




        if (50<=x<=100) and (420<=new_y<=430) :
            x1 = 20
            x2 = 50
            x3 = 200
            x4 = 230
            start_flag = True
            score_count = 0
            print(f"Starting Over! Score:{score_count}")


    glutPostRedisplay()




def animation() :


    global pause_flag


    if (pause_flag == False)  :
        glutPostRedisplay()
        


def iterate() :
    glViewport(0,0,500,500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0,500,0.0,500,0.0,1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen() :
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()


    draw_catcher()
     
    left_arrow()
    cross()


    #global fall_speed
    global score_count, over_flag 
   
    for d in diamond_arr :
        d[1] += fall_speed
        
        draw_diamond(d[0],d[1])


        if (d[1] > 500) :
            d[1] = 0
        


    if (pause_flag == True) :
        pause()
    else :
        play()
   
    if (over_flag == True) :
        glutLeaveMainLoop()
   


    glutSwapBuffers()






for i in range(5):
    x = random.uniform(-500,500)
    y = random.uniform(0,500)
    diamond_arr.append([x,y])


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500,500)
glutInitWindowPosition(0,0)
wind = glutCreateWindow(b"Diamond Game")
glutDisplayFunc(showScreen)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)
glutIdleFunc(animation)
glutMainLoop()
