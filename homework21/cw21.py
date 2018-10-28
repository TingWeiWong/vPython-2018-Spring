from visual import*
from visual.graph import *
# (Your parameters here)
R,L,C=30,200*10**-3,20*10**-6
VC,VL,VR=0,0,0
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
I_theory,phase_theory=0,0
while t*fd<8:
    rate(10000)
    Q+=i*dt
    VC=Q/C
    VR=i*R
    v=36*sin(omega*t)    
    VL=v-VR-VC
    di=VL*dt/L
    i+=di
    E=0.5*C*VC**2+0.5*L*i**2
    t+=dt
    if t*fd>6 and i<I1 and count==0:
        I_result=i
        count+=1
    if count==1 and I1<i:
        count+=1
    if count==2 and i<I1:
        t2=t
        count+=1
    if count==3 and v_low>v:
        t3=t-t2
        count+=1
    if t*fd>8 and  p==0:
        p+=1
        E2=E
    v_low=v    
    I1=i
    i_t.plot(pos=(t,i))
    v_t.plot(pos=(t,v/100))
    E_t.plot(pos=(t,E))
    I_theory=36/sqrt(R**2+(L*omega-1/(omega*C))**2)
    phase_theory=atan((L*omega-1/(omega*C))/R)/2/pi*360
print 'Theoretically, I =',I_theory,"Phase angle =", phase_theory
print 'In reality I = ',I_result, 'Phase angle = ', -t3*60*360#angle
print 'Error I =',(I_theory-I_result)/(I_theory)*100,'percent    Phase angle =',((phase_theory)+t3*60*360)/(phase_theory)*100,"percent"

while t*fd<13:
	rate(1E4)
	#(your calculations here)
	Q+=i*dt
	i+=di
	v=0
	VR=i*R
	VC=Q/C
	VL=-VR-VC
	di=dt*VL/L
	E=0.5*C*VC**2+0.5*L*i**2
	i_t.plot(pos=(t,i))
	v_t.plot(pos=(t,v/100))
	E_t.plot(pos=(t,E))
	t+=dt
	if E<=0.1*E2 and p==1:
		t4=t
		p=2
print "Decay time =",t4*fd-8