from visual import *
pi=3.1415926535
rr=0.06
R=0.12
z=0.30
meu0=4*pi*10**-7
dr=0.001
dtheta=5
# BBB=0
def B(r1,r2):
    B=vector(0,0,0)
    d=(r1-r2)
    B=meu0*1/4/pi/mag2(d)
    return B

def flux(r1,r2,h1,h2):
    flux=0    
    dtheta=0.01
    for x in arange(0,r1+dr,dr):
        for theta in arange(0.0,2*pi+dtheta,dtheta):
            pos=(vector(r2*cos(theta),h2,r2*sin(theta)))
            dflux=B(vector(x,h1,0),pos)*dr*r2*dtheta
            flux+=dflux*2*pi/100.0
    return flux


print "flux =",flux(R,rr,z,0)
print "flux =",flux(rr,R,0,z) 
    
    
