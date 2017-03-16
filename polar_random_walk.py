#polar random walk
import turtle, math, random

ted = turtle.Turtle()
wn = turtle.Screen()
wh = wn.window_height()
ww = wn.window_width()
ted.speed(30)

def simulate(n, radius=100, angle=360):
    point = []
    curr_pos = ted.position()
    for i in range(n):
        c = i/float(n)
        # should set color vector to random functions
        vec = (c**2,1-c,1-c)
        ted.pencolor(vec)
        r = random.random()*radius #edit radius
        theta = random.random()*angle #edit angle
        ted.forward(r)
        # movement condition
        # if i%2 ==0:
        #     ted.left(theta)
        # else:
        #     ted.right(theta)
        ted.left(theta-180)
        #store positions
        point.append(curr_pos)
        if curr_pos in point:
            ted.dot()
        # wrap around - boundary conditions
        p = ted.position()
        if p[0] < -ww/2:
            ted.penup()
            ted.setposition(p[0]+ww,p[1])
            ted.pendown()
        elif p[0] > ww/2:
            ted.penup()
            ted.setposition(p[0]-ww,p[1])
            ted.pendown()
        elif p[1] < -wh/2:
            ted.penup()
            ted.setposition(p[0],p[1]+wh)
            ted.pendown()
        elif p[1] > wh/2:
            ted.penup()
            ted.setposition(p[0],p[1]-wh)
            ted.pendown()


simulate(500, 100, 360)


turtle.done()
