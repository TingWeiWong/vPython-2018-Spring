from visual import *
N = 100 # You can change this for faster calculation or better resolution
R = 1.0
lamda = 500E-9
d = 100E-6
distance=50
dx = d/N
dy = d/N
scene1 = display(title='Real Image', height=600, width=600, center = (N*dx/2, N*dy/2, 0))
scene2 = display(title='Not Real',x=600, height=600, width=600, center = (N*dx/2, N*dy/2, 0))
side = linspace(-0.01*pi, 0.01*pi, N)
x,y = meshgrid(side,side)
kx=2*pi*x/lamda
ky=2*pi*y/lamda
X_range=[d*n/50.0 for n in range(-1*distance,distance+1)]
Y_range=[d*n/50.0 for n in range(-1*distance,distance+1)]

E_field=(0j*n)
for X in X_range:
    for Y in Y_range:
         if (X*X+Y*Y) <(d/2.0)**2:
             phase=kx*X+ky*Y
             E_field+=exp(phase*1j)
Inte = abs(E_field)**2
maxI = amax(Inte)
minI = amin(Inte)
for i in range(N):
     for j in range(N):
         point = box(display = scene1, pos=(i*dx, j*dy, 0), length = dx, height= dy, width = dx,
         color=(Inte[i,j]/maxI,Inte[i,j]/maxI,Inte[i,j]/maxI))
         del point


Inte = abs(E_field)**0.2
minI = amin(Inte)
maxI = amax(Inte)


count=0
resulta=0.0
counta=0.0
for i in range(N):
     for j in range(N):
         point = box(display = scene2, pos=(i*dx, j*dy, 0), length = dx, height= dy, width = dx,
         color=(Inte[i,j]/maxI,Inte[i,j]/maxI,Inte[i,j]/maxI))
         if  Inte[i,j]<minI+0.8 and 46<=i<=54:
             count=((i-50)**2+(j-50)**2)**0.5
             if count<15:
                 resulta+=count
                 counta+=1
         del point
print "Angle =",resulta/counta/R*dx*N*2*pi
print "Theta =",asin(1.22*lamda/d)
print "Error =",(resulta/counta/R*dx*N*2*pi-asin(1.22*lamda/d))/asin(1.22*lamda/d)*100,"%"

Inte = abs(E_field)
minI = amin(Inte)
maxI = amax(Inte)

for i in range(N):
     for j in range(N):
         point = box(display = scene2, pos=(i*dx, j*dy, 0), length = dx, height= dy, width = dx,
         color=(Inte[i,j]/maxI,Inte[i,j]/maxI,Inte[i,j]/maxI))
         del point
