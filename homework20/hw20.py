from visual import *
import math
pi=math.pi
r=0.06
R=0.12
z=0.30
u=4*pi*10**-7
ds=1E-3
def B(r1,r2):
    B=vector(0,0,0)
    d=(r1-r2)
    B=u*1/4/pi/abs(d)**2
    return B

def flux(r1,r2,h1,h2):
    flux=0    
    dtheta=0.01
    for x in arange(0,r1+ds,ds):
        for theta in arange(0.0,2*pi+dtheta,dtheta):
            pos=(vector(r2*cos(theta),h2,r2*sin(theta)))
            dflux=B(vector(x,h1,0),pos)*ds*r2*dtheta
            flux+=dflux*2*pi/100.0
    return flux


print "Flux on height 30 plain =",flux(R,r,z,0)
print "Flux on the bottom plain =",flux(r,R,0,z) 
    
    
