from visual import*
from visual.graph import*

scene1=gdisplay(title='Earth Time',y=400,width=800,height=300,xtitle="Time",ytitle='Speed/C',background=(0.5,0,0.5))
x=gcurve(color=(random.random(),random.random(),0),gdisplay=scene1)

scene2=gdisplay(title='Space Ship Time',y=100,width=800,height=300,xtitle="Time",ytitle='Speed/C',background=(0,0.5,0.7))
x1=gcurve(color=color.red,gdisplay=scene2)
g=9.8 #Gravity constant
dt=100000 
c=3E8 #Speed of light
lightyear=365.25*86400*c 
v=0
a=g*dt #Terminal Speed
d=0
t=0
t_prime=0
stage=0
while true:
    rate(2000)
    if d<7.5*lightyear:
        g=9.8
    elif d>7.5*lightyear:
        g=-9.8
    d+=v*dt
    v += g * (1-v*v/c/c)**1.5 * dt
    if a*v<0 :
        stage+=1
    a=v
    t+=dt
    t_prime+=dt*sqrt(1-v*v/c/c)
    x.plot(pos=(t/86400.0/365.25,v/c))
    x1.plot(pos=(t_prime/86400.0/365.25,v/c))
    
    if stage==2:
        print "Earth Time ",t/86400.0/365.25
        print "Space Time ",t_prime/86400.0/365.25
        break    

    
