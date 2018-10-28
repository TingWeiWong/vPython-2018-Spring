from visual import*
from visual.graph import*

def reflection_vector(v_in, normal_v):
    v_out = -rotate(v_in, pi, normal_v)
    return v_out

def refraction_vector(n1, n2, v_in, normal_v):
    theta = diff_angle(v_in, normal_v)
    phi = arcsin(n1*sin(theta)/n2)
    v_out = rotate(v_in, theta-phi, cross(v_in, normal_v))
    return v_out

scene2 = gdisplay(x=0, y=400, width=1000, height=400, xtitle='b', ytitle='Theta', background=(0.2, 0.6, 0.2))
theta_b_red = gcurve(color=color.red, gdisplay=scene2)
theta_b_blue = gcurve(color=color.blue, gdisplay=scene2)


delta=0.001
for i in range (200):
    b=0.01*i
    for (light_color, n_water) in [(color.red, 1.331), (color.blue, 1.339)]:
        light_pos=vector(-5,b,0)
        light_v=vector(1.0,0,0)
        stage=0
        delta=0.01
        while true:
            rate(100000)
            light_pos+=light_v*delta
            if abs(light_pos)<=2 and stage==0:
                light_v=refraction_vector(1,n_water,light_v,-light_pos)
                stage=1
            if abs(light_pos)>=2 and stage==1:
                light_v=reflection_vector(light_v,-light_pos)
                stage=2
            if abs(light_pos)>=2 and stage==2 and light_pos.y<0:
                light_v=refraction_vector(n_water,1,light_v,light_pos)
                stage=3
            if abs(light_pos)>5 and light_v.x<0:
                if n_water == 1.331: theta_b_red.plot(pos=(b, diff_angle(light_v, vector(-1, 0, 0)) / pi * 180))
                else: theta_b_blue.plot(pos=(b, diff_angle(light_v, vector(-1, 0, 0)) / pi * 180))
                if b == 1.78:
                    if n_water == 1.331: print "Red = ", diff_angle(light_v, vector(-1, 0, 0)) / pi * 180
                    else: print "Blue = ", diff_angle(light_v, vector(-1, 0, 0)) / pi * 180
                break