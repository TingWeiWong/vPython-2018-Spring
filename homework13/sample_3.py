from visual import *
k=8.99*10**9
L,size=1.0,0.1
polecharge,poleposition,polecolor=[-1E-5,-1E-5,1E-5,1E-5],[vector(L,0,0),(-L,0,0),(0,L,0),(0,-L,0)],[(0,0,1),(0,0,1),(1,0,0),(1,0,0)]
ball_m,ball_q=1E-6,1E-12
N=0

scene=display(title='dipole',height=500,width=500,range=3.5,auto_scale=False,background=(0.5,0.5,0))
pole_set=[sphere(pos=p,radius=size,color=cc,q=charge)for(charge,p,cc)in zip(polecharge,poleposition,polecolor)]
ball=[]
ballforce=[]
label(text='Left click to plece balls.',pos=(0,0.5,0),opacity=0.2)
def Force_E(r,q):
    r0=r-vector(L,0,0)
    r1=r-vector(-L,0,0)
    r2=r-vector(0,L,0)
    r3=r-vector(0,-L,0)
    return -k*1E-5*q/abs(r0)**2*r0.norm()-k*1E-5*q/abs(r1)**2*r1.norm()+k*1E-5*q/abs(r2)**2*r2.norm()+k*1E-5*q/abs(r3)**2*r3.norm()
def makeSphere(evt):
    loc=evt.pos
    print"click at",loc
    ball.append(sphere(pos=loc,radius=0.05,color=(1,0,1),make_trail=true,v=vector(0,0,0),a=vector(0,0,0),q=ball_q,f=vector(0,0,0)))
    print Force_E(loc,ball_q)

scene.bind('mousedown',makeSphere,scene)

dt=0.001
while true:
    rate(3000)
    for balls in ball:
        balls.a=Force_E(balls.pos,ball_q)/ball_m
        balls.v+=balls.a*dt
        balls.pos+=balls.v*dt
        if abs(balls.pos-vector(-L,0,0))<=0.1*size or abs(balls.pos-vector(L,0,0))<=0.1*size:
            balls.make_trail=false
            balls.visible=false
