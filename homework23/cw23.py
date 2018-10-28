from visual import *
scene = display(title="Ray",background=(0.8, 0.8, 0.8), width=1200, height=300, center = (3,0,10), fov = 0.004)
R = 4.0
thickness = 0.3
g1center = (-R + thickness/2.0, 0, 0)
g2center = (R-thickness/2.0, 0, 0)
curve_range = [0.005 * t for t in range(259,314)]
lens_surface1 = [(R*cos(theta), R *sin(theta) ) for theta in curve_range]
circle1 = paths.arc(pos=g1center, radius=0.0000001, angle2=2*pi, up = (1,0,0))
lens_surface2 = [(-R*cos(theta),-R *sin(theta) ) for theta in curve_range]
circle2 = paths.arc(pos=g2center, radius=0.0000001, angle2=2*pi, up = (1,0,0))
extrusion(pos=circle1, shape=lens_surface1, color=color.yellow)
extrusion(pos=circle2, shape=lens_surface2, color=color.yellow)
curve(pos=[(-7,0,0),(13,0,0)], color=color.red, radius = 0.02)
arrow(pos=(-6,0,0), axis=(0,0.25,0), shaftwidth=0.1)
arrow(pos=(12,0,0), axis=(0,-0.25/6.0*12,0), shaftwidth=0.1)

k=0.3
def refraction(n1, n2, v_in, normal_v):
    theta = diff_angle(v_in, normal_v)
    phi = arcsin(n1*sin(theta)/n2)
    v_out = rotate(v_in, theta-phi, cross(v_in, normal_v))
    return v_out
r=-5
f=0
for db in range(20):
    b = 0.1 * db
    ray = sphere(pos=(-6, 0.25, 0), color=(0.5,0.5,1), radius=0.01, make_trail=True)
    ray.trail_object.radius = 0.01
    k=0.5
    ray.v = vector(1.0,sin(k/13.0)-sin(b/13.0), 0)
    count = 0
    

    dt = 0.5
    while True:
        rate(100000)
        ray.pos += ray.v * dt
        if abs(ray.pos-vector(R-thickness/2.0, 0, 0)) <= (R) and count == 0:
            ray.v = refraction(1, 1.5, ray.v, (-ray.pos+vector(R-thickness/2.0, 0, 0)))
            count = 1
            dt=0.01
        if abs(ray.pos-vector(-R+thickness/2.0, 0, 0)) >= R and count == 1:
            ray.v = refraction(1.5, 1, ray.v, -(-ray.pos+vector(-R+thickness/2.0, 0, 0)))
            count = 2
        if db==k*10 and count==2 and ray.pos.y<0:
            dt=3
            f=ray.pos.x
            q=1/(1/f-1/6.0)
            count=3
            
            

        if db!=k*10 and count==2:
            count=3
            dt=3
        if count==3 and abs(ray.pos.x-12)<1.5 and ray.pos.y>r:
            print db,ray.pos.y,ray.pos.y+0.5
        if abs(ray.pos) > 13 and count==3: break
        t+=dt
print 'Focal Point =',f               
print 'Image Point = ',q
verification=1.0/f-1.0/q
print "To verify 1/p+1/q=1/f, 1/f-1/q= ",verification,"= 1/p "
print "So the quation is verified. "