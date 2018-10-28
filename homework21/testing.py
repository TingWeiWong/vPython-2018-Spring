from visual import*
from visual.graph import *
# (Your parameters here)
C,L,R=20*10**-6,200*10**-3,30
Q=0
Vc,Vl,Vr=0,0,0
i,di=0,0
I,I1=0,0
ii,vv=-1,-1
k,p=0,0
t1,t2,t3,t4=0,0,0,0
fd = 60.0
wd=2*pi*fd
E1,E2=0,0
t=0
dt = 1.0/(fd * 5000) # 5000 simulation points per period

scene1 = gdisplay(x=0, y=0, width=1000, height=400, xtitle='t', ytitle='i blue, v red,', background=(0.2, 0.6, 0.2))
scene2 = gdisplay(x=0, y=400, width=1000, height=400, xtitle='t', ytitle='Energy', background=(0.2, 0.6, 0.2))
i_t = gcurve(color=color.blue, gdisplay = scene1)
v_t = gcurve(color=color.red, gdisplay = scene1)
E_t = gcurve(color=color.red, gdisplay = scene2)
while t * fd < 8:
    rate(10000)
    Q+=i*dt
    Vc=Q/C
    Vr=i*R
    Vl=36*sin(2*pi*fd*t)-Vr-Vc
    di=Vl*dt/L
    i+=di
    v=36*sin(2*pi*fd*t)
    E=Q*Q/C/2+i*i/2*L

    t+=dt
    if t*fd>5 and i<I1 and k==0:
        I=i
        k=1 
    if k==1 and I1<i:
        k=2
    if k==2 and i<I1:
        t2=t
        k=3
    if k==3 and vv>v:
        t3=t-t2
        k=4
    if t*fd>8 and  p==0:
        p=1
        E2=E
    vv=v    
    I1=i

    i_t.plot(pos=(t,i))
    v_t.plot(pos=(t,v/100))
    E_t.plot(pos=(t,E))
print 'In theorem, I =',36/sqrt(R**2+(L*wd-1/(wd*C))**2),"phase angle =", atan((L*wd-1/(wd*C))/R)/2/pi*360
print 'I = ',I, 'phase angle = ', -t3*60*360#angle
print 'error I =',(36/sqrt(R**2+(L*wd-1/(wd*C))**2)-I)/(36/sqrt(R**2+(L*wd-1/(wd*C))**2))*100,'percent    phase angle =',((atan((L*wd-1/(wd*C))/R)/2/pi*360)+t3*60*360)/(atan((L*wd-1/(wd*C))/R)/2/pi*360)*100,"percent"
p=1
while t * fd < 13:
    rate(10000)
    Q+=i*dt
    Vc=Q/C
    Vr=i*R
    Vl=-Vc-Vr
    di=Vl*dt/L
    i+=di
    v=0
    E=Q*Q/C/2+i*i/2*L
    # (your calculation here)
    i_t.plot(pos=(t,i))
    v_t.plot(pos=(t,v/100))
    E_t.plot(pos=(t,E))
    t+=dt
    if E<=0.1*E2 and p==1:
     t4=t
     p=2
print "time =",t4*fd-8,"T (",t4-8/60.0,"s)","(from 8T)"
