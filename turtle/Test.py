import turtle
import math

def square(t,length):
    for x in range(4):
        t.fd(length)
        t.lt(90)
        
def polyline(t,n,length,angle):
    for x in range(n):
        t.fd(length)
        t.lt(angle)   

def polygon(t,n,length):
    polyline(t,n,length,360/n)    

def arc(t,r,angle):
    acr_length=2*math.pi*r*(angle/360)
    n = int(acr_length / 4) + 1
    step_length = acr_length / n
    step_angle = float(angle) / n
    t.lt(step_angle/2)
    polyline(t,n,step_length,step_angle)
    t.rt(step_angle/2)

def circle(t,r):
    arc(t,r,360)

if __name__ == '__main__':
    bob=turtle.Turtle()
    # square(bob,100)
    # polygon(bob,5,100)
   

    turtle.mainloop()
    

    
