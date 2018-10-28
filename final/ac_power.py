from visual import*
from visual.graph import *
# (Your parameters here)
R=30
fd = 60.0
omega=2*pi*fd
Q=0.0
di,i=0.0,0.0
I1=0
p=0
t = 0.0
dt = 1.0/(fd * 5000) # 5000 simulation points per period
scene1 = gdisplay(x=0, y=0, width=1000, height=400, xtitle='t', ytitle='Current blue, Voltage red,', background=(0.2, 0.6, 0.2))
scene2 = gdisplay(x=0, y=400, width=1000, height=400, xtitle='t', ytitle='Energy', background=(0.2, 0.6, 0.2))
i_t = gcurve(color=color.blue, gdisplay = scene1)
v_t = gcurve(color=color.red, gdisplay = scene1)
E_t = gcurve(color=color.red, gdisplay = scene2)
count=0
v_low=0
while t*fd<8:
    rate(10000)
    v=36*sin(omega*t)    
    loss=0.5*v**2/R
    t+=dt
    v_low=v    
    I1=i
    i_t.plot(pos=(t,i))
    v_t.plot(pos=(t,v/100))
    E_t.plot(pos=(t,loss))
