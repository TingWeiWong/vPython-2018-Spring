from visual import *
from visual.graph import *

pi=3.1415926535
R=0.5 # Radius of inductor
u0=4*pi*1E-7
loop=5 # Loop of wire on the inductor
NL=6 # Number of inductor
l=4 # Lenth of inductor in metres
A=pi*R*R  # Area of the inductor
L=u0*loop**2*A*l # The induction constant of inductor
dis=3 # Distance from  magnet

Bmag= 1  # Unit= Telsa, the intensity of the magnet
Mag = cylinder(pos=(0,0,0),axis=(1,0,0),radius=1) # Magnet in cylinder
fd=6000  # 60 Hz for the rotation of magnet
omega=2*pi*fd # Omega 
dtheta=0.1 # 
dt=dtheta/omega
t=0
#curve
scene2 = gdisplay(x=0, y=0, width=1000, height=400, xtitle='t', ytitle='v', background=(0.2, 0.6, 0.2))
v_t = gcurve(color=color.red, gdisplay = scene2)
inductors=[]
#inductors
for i in range(NL):
    inductors.append(cylinder(pos=(dis*cos(2*pi*i/NL),dis*sin(2*pi*i/NL),0),axis=(l*cos(2*pi*i/NL),l*sin(2*pi*i/NL),0),radius=R))

#find mag flux
def flux(posL,Baxis,Laxis):
    flux=0
    d=abs(posL-Baxis)
    flux=Bmag*abs(cos(diff_angle(Baxis,Laxis)))*A/d
    return flux
    
def V(posL,Baxis,Laxis):
    V=0
    flux0=0
    flux1=0
    flux0=flux(posL,Baxis,Laxis)
    Baxis2=rotate(Baxis,angle=0.1,axis=(0,0,1))
    flux1=flux(posL,Baxis2,Laxis)
    V=(flux1-flux0)/dt
    return V
# while(true):
#     t+=dt
#     Vt=0
#     for i in range(NL):
#         posL=vector(dis*cos(2*pi*i/NL),dis*sin(2*pi*i/NL),0)
#         Laxis=(l*cos(2*pi*i/NL),l*sin(2*pi*i/NL),0)
#         Vl=V(posL,Mag.axis,Laxis)
#         Vt+=Vl
#         # print Mag.axis
#     v_t.plot(pos=(t,Vt))
#     Baxis=Mag.axis
#     Mag.axis = rotate(Baxis,angle=0.1,axis=(0,0,1))
theta=0
while True:
    rate(100)
    theta+=dtheta
    epsilon=0
    Mag.axis=vector(cos(theta),sin(theta),0)
    for i in range(NL):
        epsilon+=V(inductors[i].pos,Mag.axis,inductors[i].axis)
    v_t.plot(pos=(t,epsilon))















