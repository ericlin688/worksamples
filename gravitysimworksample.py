#gravitational simulator
#with dynamic black hole at center
#particle collision

#imports
import turtle
from random import randint
from math import sqrt

#setup screen and black hole
screen=turtle.Screen()
screen.setup(width=1000,height=1000)
screen.tracer(0)
screen.colormode(255)
hole=turtle.Turtle()
hole.hideturtle()

#initialize list of satillites
s=[]

#set global variables and initial conditions
t=0.05
T=int(t*1000)
mh=2000
G=50
r=G*mh/10000

#on left click, create masses
#randomize the color, mass and velocity of each
def clicky(x,y):
    screen.onclick(None)
    for i in range(40):
        p=turtle.Turtle()
        p.color(randint(0,255),randint(0,255),randint(0,255))
        p.x=randint(-500,500)
        p.y=randint(-500,500)
        p.pu()
        p.goto(p.x,p.y)
        #p.pd() #show orbital paths
        p.shape('circle')
        p.v=randint(-60,60)
        p.w=randint(-60,60)
        p.m=randint(10,500)
        p.turtlesize(p.m/500+1/10)
        p.a=0
        s.append(p)
    screen.update()
    screen.onclick(clicky)
    return

#If black hole has consumed mass, change size
def hole_update():
    global r
    r=G*mh/10000
    hole.pu()
    hole.goto(0,-r)
    hole.pd()
    hole.begin_fill()
    hole.circle(r)
    hole.end_fill()
    return

#Runs simulation
def tt():
    screen.onclick(None)
    global mh
    i=0
    while i<len(s):
        s[i].a=-G*mh/(s[i].x**2+s[i].y**2)**(3/2)
        nl=s[0:i]+s[i+1:len(s)]
        if len(nl)>len(set(nl)): #delete last x elements of list
            nl=nl[0:len(set(nl))-1]
        n=s[i]
        as_=0
        vs=0
        ws=0
        j=0
        temp2=False
        while j<len(nl):
            as_=-G*n.m/((nl[j].x-n.x)**2+(nl[j].y-n.y)**2)**(3/2)
            vs+=(n.x-nl[j].x)*as_*t
            ws+=(n.y-nl[j].y)*as_*t
            j+=1
        if temp2:
            continue
        s[i].v+=s[i].x*s[i].a*t+vs
        s[i].x+=s[i].v*t
        s[i].w+=s[i].y*s[i].a*t+ws
        s[i].y+=s[i].w*t
        s[i].goto(s[i].x,s[i].y)
        if abs(s[i].x)>500 or abs(s[i].y)>500:
            s[i].clear()
            s[i].hideturtle()
            del s[i]
            i-=1
        elif sqrt(s[i].x**2+s[i].y**2)<r:
            s[i].clear()
            s[i].hideturtle()
            mh+=s[i].m
            hole_update()
            del s[i]
            i-=1
        i+=1
    screen.update()
    screen.ontimer(tt,T)
    screen.onclick(clicky)
    return

#function calls to start sim
screen.onclick(clicky)
hole_update()
tt()
screen.mainloop()