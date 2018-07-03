import turtle
 
def draw(t,length,n):
    if n==0:
        return
        pass
    angle=50
    t.fd(length*n)
    t.lt(angle)
    draw(t,length,n-1)
    t.rt(angle*2)
    draw(t,length,n-1)
    t.lt(angle)
    t.bk(length*n)

    pass

def dawline_koch(t,x):
    if x<3:
        t.fd(x)
        return
        pass
    dawline_koch(t,x/3)
    t.lt(60)
    dawline_koch(t,x/3)
    t.rt(120)
    dawline_koch(t,x/3)
    t.lt(60)
    dawline_koch(t,x/3)
    pass

if __name__ == '__main__':
    bob=turtle.Turtle()
    dawline_koch(bob,500)
    turtle.mainloop()