import turtle

bob = turtle.Turtle()

bob.speed(10)

def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

theta = 137.508
c = 1
#radius = c*theta**0.5
r = 0
g = 0
b = 0
for radius in range(500):
    r = radius/500.0
    g = radius/500.0
    b = radius/500.0
    bob.pencolor((r,g,b))
    bob.dot()
    bob.penup()
    bob.left(theta)
    bob.forward(c*radius)

turtle.done()
