from visual import *
from visual.graph import *

pi=3.1415926535
meu0=4*pi*10**-7
MagS = cylinder(pos=(5,0,0),axis=vector(1,0,0),radius=3,color=color.blue)
Mag = cylinder(pos=(-5,0,0),axis=vector(-1,0,0),radius=3,color=color.red)
B = vector(10,0,0)
fd=60
omega=2*pi*fd
dtheta=0.1
dt=dtheta/omega
t=0
r=0.001 # resistance of the coil

#loop
loop_c = curve(pos=[(0,-1,-1),(0,-1,1),(0,1,1),(0,1,-1),(0,-1,-1)])
Loop = ring(pos=(0,0,0), axis=(1,0,0), radius=1, thickness=0.1, opacity=0)
A = 4
theta = 0

#curve
scene1 = gdisplay(x=0, y=0, width=1000, height=400, xtitle='t', ytitle='v', background=(0.2, 0.6, 0.2))
scene2 = gdisplay(x=0, y=400, width=1000, height=400, xtitle='t', ytitle='power', background=(0.2, 0.6, 0.2))
v_t = gcurve(color=color.red, gdisplay = scene1)
i_0 = gcurve(color=color.red, gdisplay = scene1)
i_1 = gcurve(color=color.blue, gdisplay = scene1)
i_2 = gcurve(color=color.green, gdisplay = scene1)
p = gcurve(color=color.yellow, gdisplay = scene2)
p2 = gcurve(color=color.cyan, gdisplay = scene2)

#find mag flux
def flux(Laxis):
    flux=0
    flux=B.dot(A*Laxis.norm())
    return (flux)
    
def V(Laxis):
    V=0
    flux0=0
    flux1=0
    flux0=flux(Laxis)
    Laxis2=rotate(Laxis,angle=0.1,axis=(0,1,0))
    flux1=flux(Laxis2)
    V=(flux1-flux0)/dt
    return V

while(true):
    rate(25)
    t+=dt
    Vt=0
    u=vector(0,0,0)
    tor=vector(0,0,0)
    Laxis=Loop.axis
    Vt=V(Laxis)
    #tor = Vt/r*A*norm(Laxis).cross(B)#F=iAxB
    power=0
    power+=Vt**2/r
    u=Vt/r*A*Laxis.norm() #megnetic moment
    tor=u.cross(B) 
    p.plot(pos=(t,omega*tor.y))     #yellow  power consumed to rotate the magnet
    p2.plot(pos=(t,power))          #cyan       output power 
    if(tor.y!=0):
        print 'p_out/p_in = ',power/(omega*tor.y)
    v_t.plot(pos=(t,Vt))
    Loop.axis=rotate(Laxis,angle=0.1,axis=(0,1,0))
    theta += 0.1
    loop_c.pos=[(2*cos(-pi/2-theta),-1,2*sin(-pi/2-theta)),(2*cos(pi/2-theta),-1,2*sin(pi/2-theta)),(2*cos(pi/2-theta),1,2*sin(pi/2-theta)),(2*cos(-pi/2-theta),1,2*sin(-pi/2-theta)),(2*cos(-pi/2-theta),-1,2*sin(-pi/2-theta))]

