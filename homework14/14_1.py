from visual import *
epsilon0=8.8542E-12
k=1.0/(4*pi*epsilon0)
lambda0,RodR,RodL=1E-6,0.02,1.0 #Charged Rod parameters
R,L=0.5,1.4 #Tube radius and length
ball_m,ball_q=1E-6,1E-12

def E(r):
	result=vector(0,0,0)
	for x in range(100):
		position=vector(x*0.01-0.5,0,0)
		direction=r-position
		dE=lambda0*k*0.01*cos(pi*(x*0.01-0.5))*abs(direction)**(-2)*direction.norm()
		result+=dE
	return result

scene=display(title='Charged rod', x=0 ,y=0, width=600, height=600, background=(0.5,0.5,0.5))
rod=cylinder(pos=(-RodL/2.0,0,0),axis=(RodL,0,0),radius=RodR,color=color.yellow)
tube=cylinder(pos=(-L/2.0,0,0),axis=(L,0,0),radius=R,color=color.blue,opacity=0.40)
ball=[]
size=0.001
for i in range(25):
	x=0.04*i-0.5
	ball_position1=vector(x,0.01,0)
	ball_position2=vector(x,-0.01,0)
	ball.append(sphere(pos=ball_position1, radius=size, make_trail=True,v=vector(0,0,0),a=vector(0,0,0)))
	ball.append(sphere(pos=ball_position2, radius=size, make_trail=True,v=vector(0,0,0),a=vector(0,0,0)))

flux = 0    
for x in range(140):
    flux+=8*abs(E(vector(x*0.01-0.7,R,0)))*2*pi*R*0.001
for x in range(50):
    flux+=8*abs(E(vector(L/2.0,x*0.01,0)))*2*pi*x*0.01*0.001

# Calculate the total charge on the rod
Q = 0
dx=0.01
for x in  arange(-RodL/2.0,RodL/2.0+dx,dx):
    Q+=dx*lambda0*(cos(pi*x/RodL))**2

print "flux =",flux
print "Q/epsilon0 =",Q/epsilon0
print "Error percentage = ",(flux-(Q/epsilon0))/(Q/epsilon0)*100,"%"


dt=0.01
while True:
	rate(10000)
	for balls in ball:
		balls.a=E(balls.pos)*ball_q/ball_m
		balls.pos+=balls.a*dt
		if abs(balls.pos)>1.5:
			balls.make_trail=false
			balls.visible=false




