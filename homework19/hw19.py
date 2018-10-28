from visual import *
q = 1.6 * 10 ** -19
dt = 1*10**-12
BNP = vector(0, -1*10**-8, 0)
BSP = vector(0, 1*10**-8, 0)
Bcharge = 10**-8
mass = 1.67 * 10 ** -27

def B(r):
	north=r-BNP
	south=r-BSP
	n=1E-7*Bcharge*north.norm()/abs(north)**2
	s=1E-7*Bcharge*south.norm()/abs(south)**2
	return n-s


scene = display(title='Lorentz force', width=600, height=600, background=(0,0,0))
atom = sphere(pos=(0,0,1*10**-8),radius=10**-10,color=color.white) #4 initial position
N = sphere(pos=BNP,radius=10**-9,color=color.blue)
S = sphere(pos=BSP,radius=10**-9,color=color.red)


atom.velocity = vector(1*10**-2, 90*10**-3, 0) #3 different initial velocity
atomtrail = curve(color=atom.color)


while true:
	rate(30000)
	atomtrail.append(pos=atom.pos)
	a = q * cross(atom.velocity , B(atom.pos)) / mass
	atom.pos = atom.pos + atom.velocity * dt
	atom.velocity = atom.velocity + a * dt

