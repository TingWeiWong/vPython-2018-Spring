from visual import *
from visual.graph import *

pi=3.1415926535
R=1 #radius of inductor
meu0=4*pi*10**-7
N=5 #num of all turns
NL=6 #num of inductors
l=4 #lenth of coil in metres
A=pi*R*R
L=meu0*N*N*A/l
dis=3 #distance from the magnetic
r=0.001 # resistance of the coil
u=10 #magnitude of the magnetic moment

fd=60
omega=2*pi*fd
dtheta=0.1
dt=dtheta/omega
t=0

scene = display(x=1000,y=0,background=(0.5,0.5,0))

#curve
scene1 = gdisplay(x=0, y=0, width=1000, height=400, xtitle='t', ytitle='v', background=(0.2, 0.6, 0.2))
scene2 = gdisplay(x=0, y=400, width=1000, height=400, xtitle='t', ytitle='power', background=(0.2, 0.6, 0.2))
Mag = cylinder(pos=(0,0,0),axis=vector(1,0,0),radius=1,color=color.red)
MagS = cylinder(pos=(0,0,0),axis=vector(-1,0,0),radius=1,color=color.blue)
v_t = gcurve(color=color.red, gdisplay = scene1)
i_0 = gcurve(color=color.red, gdisplay = scene1)
i_1 = gcurve(color=color.blue, gdisplay = scene1)
i_2 = gcurve(color=color.green, gdisplay = scene1)
p = gcurve(color=color.yellow, gdisplay = scene2)
p2 = gcurve(color=color.cyan, gdisplay = scene2)

#inductors
for i in range(NL):
    inductors = cylinder(pos=vector(dis*cos(2*pi*i/NL),dis*sin(2*pi*i/NL),0),axis=(1*cos(2*pi*i/NL),1*sin(2*pi*i/NL),0),radius=R)

#find B of small megnet
def B(r,Baxis):
    B=meu0/(4*pi*abs(r)**3)*(3*(u*Baxis.norm()).dot(r.norm())*r.norm()-u*Baxis.norm()) 
    return B

#find B of coils
def Bcoil(V,r,d,Laxis):
    ucoil=N*V/r*A
    B=meu0/(4*pi*abs(d)**3)*(3*(ucoil*Laxis.norm()).dot(d.norm())*d.norm()-ucoil*Laxis.norm())
    return B
    
#find mag flux
def flux(posL,Baxis,Laxis):
    flux=0
    flux=B(posL,Baxis).dot(A*Laxis.norm())
    return (flux)
    #flux=Bmag*abs(cos(diff_angle(Baxis,Laxis)))*A/d
    #return flux
    
def V(posL,Baxis,Laxis):
    V=0
    flux0=0
    flux1=0
    flux0=flux(posL,Baxis,Laxis)
    Baxis2=rotate(Baxis,angle=0.1,axis=(0,0,1))
    flux1=flux(posL,Baxis2,Laxis)
    V=(flux1-flux0)/dt
    return V
while(true):
    rate(250)
    t+=dt
    Vt=0
    tor=vector(0,0,0)
    power=0
    for i in range(NL):
        posL=vector(dis*cos(2*pi*i/NL),dis*sin(2*pi*i/NL),0)
        Laxis=vector(l*cos(2*pi*i/NL),l*sin(2*pi*i/NL),0)
        #if(i==0):            ##find the current of coils
         #   i_0.plot(pos=(t,(V(posL,Mag.axis,Laxis)-V(posL,MagS.axis,Laxis))/r))
        #if(i==1):
         #   i_1.plot(pos=(t,(V(posL,Mag.axis,Laxis)-V(posL,MagS.axis,Laxis))/r))
        #if(i==2):
         #   i_2.plot(pos=(t,(V(posL,Mag.axis,Laxis)-V(posL,MagS.axis,Laxis))/r))
        V1=V(posL,Mag.axis,Laxis)
        power+=(V1)**2/r
        Vt+=V1
        tor+=u*Mag.axis.norm().cross(Bcoil(V1,r,-posL-0.5*Laxis,Laxis))
    p.plot(pos=(t,omega*tor.z))#yellow  power consumed to rotate the magnet
    p2.plot(pos=(t,power))#cyan       output power
    v_t.plot(pos=(t,Vt))
    print 'p_out/p_in = ',power/(omega*tor.z)
    Baxis=Mag.axis
    Mag.axis = rotate(Baxis,angle=0.1,axis=(0,0,1))
    MagS.axis = -Mag.axis
    