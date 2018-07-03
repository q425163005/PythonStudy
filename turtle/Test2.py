import turtle
from Test import arc

def petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        t.lt(180-angle)


def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        t.lt(360.0/n)


def move(t, length):
    t.pu()
    t.fd(length)
    t.pd()

def ajimide(t,r):
    for i in range(18):
        arc(t,(2*i-1)*r,90)
        pass
    pass

if __name__ == '__main__':
    bob=turtle.Turtle()
    # square(bob,100)
    # polygon(bob,5,100)
    # flower(bob,10,100,60)
    ajimide(bob,10)
    turtle.mainloop()