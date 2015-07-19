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
a = 5
b = 0.7
c = 1
#radius = c*theta**0.5

for r in range(500):
    radius = a + b*r**(1/c)
    bob.dot()
    bob.penup()
    bob.left(theta)
    bob.forward(radius)

turtle.done()
