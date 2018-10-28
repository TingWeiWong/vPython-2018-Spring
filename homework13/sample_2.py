from visual import *
k=8.99*10**9
L,size=1.0,0.1
polecharge,poleposition,polecolor=[1E-5,-1E-5],[vector(L,0,0),(-L,0,0)],[(1,0,0),(0,0,1)]
ball_m,ball_q=1E-6,1E-12
N=0

scene=display(title='dipole',height=500,width=500,range=3.5,auto_scale=False,background=(0.5,0.5,0.6))
pole_set=[sphere(pos=p,radius=size,color=cc,q=charge)for(charge,p,cc)in zip(polecharge,poleposition,polecolor)]
ball=[]
ballforce=[]
label(text='Left click to plece balls.',pos=(0,0.5,0),opacity=0.2)
def Force_E(r,q):
    r0=r-vector(L,0,0)
    r1=r-vector(-L,0,0)
    return k*1E-5*q/abs(r0)**2*r0.norm()-k*1E-5*q/abs(r1)**2*r1.norm()
def makeSphere(evt):
    loc=evt.pos
    print"click at",loc
    ball.append(sphere(visible=true,pos=loc,radius=0.05,color=(1,0,1),make_trail=true,v=vector(0,0,0),a=vector(0,0,0),q=ball_q,f=vector(0,0,0)))
    print Force_E(loc,ball_q)
for i in range(12):
    for j in range(6):
        ball.append(sphere(pos=vector(L+0.1*cos(60*j)*cos(30*i),0.1*cos(60*j)*sin(30*i),0.1*sin(60*j)),radius=0.005,color=(1,1,1),make_trail=true,v=vector(0,0,0),a=vector(0,0,0),q=ball_q,f=vector(0,0,0)))
    
        
scene.bind('mousedown',makeSphere,scene)

dt=0.001
while true:
    rate(3000)
    for items in ball:
        items.a=Force_E(items.pos,ball_q)/ball_m
        items.pos+=items.a*dt
        if abs(items.pos-vector(-L,0,0))<=size:
            items.make_trail=false
            items.visible=false
            
