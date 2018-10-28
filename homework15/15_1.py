from visual import*
N=101
dx,dy=1E-2/(N-1),1E-2/(N-1)
L,d=5E-3,2E-3
dx2=dx*dx
dy2=dy*dy
Q=0
def solve_laplacian(u,u_cond,dx,dy,Niter=800):
    V=array(u)
    for i in range(Niter):
        V[u_cond]=u[u_cond]
        V[1:-1,1:-1]=(dy2*(V[2:,1:-1]+V[:-2,1:-1])+dx2*(V[1:-1,2:]+V[1:-1,:-2]))/(2*(dx2+dy2))
    return V
def get_field(V,dx,dy):
    Ex,Ey=gradient(V)
    Ex,Ey=-Ex/dx,-Ey/dy
    return(Ex,Ey)
u=zeros([N,N])
u[N/2-int(L/dx/2.0):N/2+int(L/dx/2.0),N/2-int(d/dy/2.0)]=-100.0
u[N/2-int(L/dx/2.0):N/2+int(L/dx/2.0),N/2+int(d/dy/2.0)]=100.0
u_cond=not_equal(u,0)
V=solve_laplacian(u,u_cond,dx,dy)

scene=display(title='dipole',height=1000,width=1000,center=(N*dx/2,N*dy/2,0))
box(pos=(N*dx/2,N*dy/2-d/2-dy,0),length=L,height=dy/5,width=2*dx)
box(pos=(N*dx/2,N*dy/2+d/2-dy,0),length=L,height=dy/5,width=2*dx)
for i in range(N):
    for j in range(N):
        point=box(pos=(i*dx,j*dy,0),length=dx,height=dy,width=dx,color=((V[i,j]+100)/200,(100-V[i,j])/200,0.0))
Ex,Ey=get_field(V,dx,dy)
for i in range(1,N-1,2):
    for j in range(1,N-1,2):
        ar=arrow(pos=(i*dx,j*dy,2*dx),axis=(Ex[i,j]/6E8,Ey[i,j]/6E8,0),shaftwidth=dx/4.0,color=color.black)


epsilon0=8.8542E-12

Eda=[Ey[i,25]*dx2 for i in range(30,55)]
Q=-epsilon0*sum(Eda)*4



C_nonideal = -Q/200
print "Q = ",Q
print "C_nonideal = ",C_nonideal


epsilon0=8.8542E-12
C_ideal = epsilon0*(L*dx)/d
print "C_ideal = ",C_ideal
print "Error = ",(C_nonideal-C_ideal)




